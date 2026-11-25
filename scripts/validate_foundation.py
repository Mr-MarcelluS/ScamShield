#!/usr/bin/env python3
"""Validate planning coverage, dependencies, schema fixtures and local documentation links."""
import json
import re
from pathlib import Path
from urllib.parse import unquote
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((ROOT / path).read_text())

def main():
    plan = read('docs/planning/backlog.json')
    original = read('docs/planning/original-backlog.json')
    assert len(original) == 67 and {i['number'] for i in original} == set(range(1, 68))
    mapping = plan['reconciliation']
    assert len(mapping) == 67 and {i['number'] for i in mapping} == set(range(1, 68))
    tasks = {i['number']: i for i in plan['issues']}
    assert len(tasks) == len(plan['issues']) == 23
    milestones = {m['number'] for m in plan['milestones']}
    assert len(milestones) == 5
    for issue in tasks.values():
        assert issue['owner'] in plan['assignees']
        assert issue['milestone'] in milestones
        assert issue['acceptance'] and issue['tests'] and issue['scope'] and issue['labels']
        assert issue['effort_days'] > 0
        assert all(d in tasks and d != issue['number'] for d in issue['dependencies'])
        assert all(tasks[d]['milestone'] <= issue['milestone'] for d in issue['dependencies'])
    for item in mapping:
        assert item['successor'] in tasks
        assert item['action'] in {'edit', 'supersede', 'defer'}
        assert item['reason']
    visiting, visited = set(), set()
    def walk(n):
        assert n not in visiting, f'Dependency cycle at #{n}'
        if n in visited:
            return
        visiting.add(n)
        for dep in tasks[n]['dependencies']:
            walk(dep)
        visiting.remove(n)
        visited.add(n)
    for n in tasks:
        walk(n)
    analysis_schema = read('contracts/analysis.schema.json')
    export_schema = read('contracts/export.schema.json')
    for schema in (analysis_schema, export_schema):
        Draft202012Validator.check_schema(schema)
    analysis = Draft202012Validator(analysis_schema)
    for example in read('contracts/analysis.examples.json'):
        analysis.validate(example)
        assert all(i['endUtf16'] > i['startUtf16'] for i in example['indicators'])
    # Negative checks protect meaningful safety/version invariants.
    bad = dict(read('contracts/analysis.examples.json')[1], coverage='UNSUPPORTED')
    assert not analysis.is_valid(bad), 'Unsupported input must not look safe/covered'
    bad = dict(read('contracts/analysis.examples.json')[0], schemaVersion=2)
    assert not analysis.is_valid(bad), 'Unknown contract version accepted'
    Draft202012Validator(export_schema, format_checker=FormatChecker()).validate(read('contracts/export.example.json'))
    guidance = read('contracts/guidance.json')
    assert guidance['status'].startswith('draft-')
    allowed = {'tel:1930', 'https://cybercrime.gov.in/', 'https://sancharsaathi.gov.in/'}
    ids = [a['id'] for a in guidance['actions']]
    assert len(ids) == len(set(ids))
    for action in guidance['actions']:
        assert action['steps'] and action['title']
        assert set(action['destinations']) <= allowed
    financial = next(a for a in guidance['actions'] if a['id'] == 'financial_loss')
    assert financial['priority'] == 0 and financial['trigger'] == 'paid_yes'
    assert {'tel:1930', 'https://cybercrime.gov.in/'} <= set(financial['destinations'])
    for file in ROOT.rglob('*.md'):
        if '.git' in file.parts:
            continue
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', file.read_text()):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            local = unquote(target.split('#', 1)[0])
            assert (file.parent / local).exists(), f'Broken local link: {file.relative_to(ROOT)} -> {target}'
    print(f'PASS: {len(tasks)} owned tasks, 67 mappings, DAG, 5 milestones, contract fixtures, safety invariants, guidance destinations and local links')
    print('These checks do not validate Android implementation, live official forms or GitHub board state.')

if __name__ == '__main__':
    main()
