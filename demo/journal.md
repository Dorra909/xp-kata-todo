# Automated Test Journal

Generated: 2026-10-28T16:31:02

Tests execute against the actual Iteration 1 and Iteration 2 code.

| Version | Case | Test | Expected | Actual | Status | Stage | Bug ID | Notes |
|---|---:|---|---|---|---|---|---|---|
| 1 | N1 | Add a normal task | One task added | 1 task(s) | PASS | Manual test |  |  |
| 1 | N2 | List tasks | Two tasks listed | 2 task(s) | PASS | Manual test |  |  |
| 1 | N3 | Finish a task | Task completed | done=True | PASS | Manual test |  |  |
| 1 | N4 | Delete a task | No tasks remain | 0 task(s) | PASS | Manual test |  |  |
| 1 | N5 | Task counter | total=2, done=1 | {'total': 2, 'done': 1} | PASS | Manual test |  |  |
| 1 | 1 | Add normal title | Task accepted | 1 task(s) | PASS | Manual test |  |  |
| 1 | 2 | Empty title | Rejected with ValueError | Title accepted | FAIL | Manual test | B-EMPTY |  |
| 1 | 3 | Three spaces | Rejected with ValueError | Title accepted | FAIL | Manual test | B-WHITESPACE |  |
| 1 | 4 | Capitalized title | Task accepted | Acheter du Pain | PASS | Manual test |  |  |
| 1 | 5 | Search 'pain' | Both capitalization variants found | 1 match(es) | FAIL | Manual test | B-CASE-SEARCH |  |
| 1 | 6 | Search 'Pain' | Both capitalization variants found | 1 match(es) | FAIL | Manual test | B-CASE-SEARCH |  |
| 1 | 7 | Search cafe for Café | One match despite accent | 0 match(es) | FAIL | Manual test | B-ACCENTS |  |
| 1 | 8 | Finish unknown ID 999 | KeyError: task not found | IndexError: list index out of range | FAIL | Manual test | B-UNKNOWN-DONE |  |
| 1 | 9 | Delete unknown ID 999 | KeyError: task not found | IndexError: list assignment index out of range | FAIL | Manual test | B-UNKNOWN-DELETE |  |
| 1 | 10 | Delete ID -1 | Rejected; task preserved | 0 task(s) remain | FAIL | Manual test | B-NEGATIVE-ID |  |
| 1 | 11 | Finish ID abc / empty ID | Friendly validation error | ValueError: invalid literal for int() with base 10: 'abc' | FAIL | Demo | B-INVALID-INPUT | Tests integer conversion used by the demo server. |
| 1 | 12 | Delete first task; verify IDs | Remaining IDs stay stable | IDs before=[0, 1, 2]; after=[0, 1] | FAIL | Manual test | B-STABLE-IDS |  |
| 1 | 13 | Long title, accents, HTML-like text | Title accepted unchanged | Accepted; title length=5013 | FAIL | Manual test |  | HTML escaping in the browser is not verified by this unit test. |
| 1 | 14 | Two tasks, finish one | total=2, done=1 | {'total': 2, 'done': 1} | PASS | Manual test |  |  |
| 1 | 15 | Edit a task | Edit operation implemented | NotImplementedError: edit not implemented | FAIL | Manual test | B-EDIT |  |
| 1 | 16 | Filter completed / pending tasks | Filter operation implemented | NotImplementedError: filter not implemented | FAIL | Manual test | B-FILTER |  |
| 2 | N1 | Add a normal task | One task added | 1 task(s) | PASS | Manual test |  |  |
| 2 | N2 | List tasks | Two tasks listed | 2 task(s) | PASS | Manual test |  |  |
| 2 | N3 | Finish a task | Task completed | done=True | PASS | Manual test |  |  |
| 2 | N4 | Delete a task | No tasks remain | 0 task(s) | PASS | Manual test |  |  |
| 2 | N5 | Task counter | total=2, done=1 | {'total': 2, 'done': 1} | PASS | Manual test |  |  |
| 2 | 1 | Add normal title | Task accepted | 1 task(s) | PASS | Manual test |  |  |
| 2 | 2 | Empty title | Rejected with ValueError | ValueError: Le titre ne peut pas être vide. | PASS | Manual test |  |  |
| 2 | 3 | Three spaces | Rejected with ValueError | ValueError: Le titre ne peut pas être vide. | PASS | Manual test |  |  |
| 2 | 4 | Capitalized title | Task accepted | Acheter du Pain | PASS | Manual test |  |  |
| 2 | 5 | Search 'pain' | Both capitalization variants found | 2 match(es) | PASS | Manual test |  |  |
| 2 | 6 | Search 'Pain' | Both capitalization variants found | 2 match(es) | PASS | Manual test |  |  |
| 2 | 7 | Search cafe for Café | One match despite accent | 0 match(es) | FAIL | Manual test | B-ACCENTS |  |
| 2 | 8 | Finish unknown ID 999 | KeyError: task not found | KeyError: 'Tâche 999 introuvable.' | PASS | Manual test |  |  |
| 2 | 9 | Delete unknown ID 999 | KeyError: task not found | KeyError: 'Tâche 999 introuvable.' | PASS | Manual test |  |  |
| 2 | 10 | Delete ID -1 | Rejected; task preserved | KeyError: 'Tâche -1 introuvable.' | PASS | Manual test |  |  |
| 2 | 11 | Finish ID abc / empty ID | Friendly validation error | ValueError: invalid literal for int() with base 10: 'abc' | FAIL | Demo | B-INVALID-INPUT | Tests integer conversion used by the demo server. |
| 2 | 12 | Delete first task; verify IDs | Remaining IDs stay stable | IDs before=[1, 2, 3]; after=[2, 3] | PASS | Manual test |  |  |
| 2 | 13 | Long title, accents, HTML-like text | Title accepted unchanged | Accepted; title length=5012 | PASS | Manual test |  | HTML escaping in the browser is not verified by this unit test. |
| 2 | 14 | Two tasks, finish one | total=2, done=1 | {'total': 2, 'done': 1} | PASS | Manual test |  |  |
| 2 | 15 | Edit a task | Edit operation implemented | NotImplementedError: edit not implemented | FAIL | Manual test | B-EDIT |  |
| 2 | 16 | Filter completed / pending tasks | Filter operation implemented | NotImplementedError: filter not implemented | FAIL | Manual test | B-FILTER |  |

## Summary

- Tests executed: 42
- Passed: 25
- Failed checks: 17
- Distinct bug IDs among failed checks: 11
- Distinct bugs found after coding (stage != Writing): 11

## Bugs to investigate

- **B-ACCENTS**: Iteration 1 case 7 (Manual test); Iteration 2 case 7 (Manual test)
- **B-CASE-SEARCH**: Iteration 1 case 5 (Manual test); Iteration 1 case 6 (Manual test)
- **B-EDIT**: Iteration 1 case 15 (Manual test); Iteration 2 case 15 (Manual test)
- **B-EMPTY**: Iteration 1 case 2 (Manual test)
- **B-FILTER**: Iteration 1 case 16 (Manual test); Iteration 2 case 16 (Manual test)
- **B-INVALID-INPUT**: Iteration 1 case 11 (Demo); Iteration 2 case 11 (Demo)
- **B-NEGATIVE-ID**: Iteration 1 case 10 (Manual test)
- **B-STABLE-IDS**: Iteration 1 case 12 (Manual test)
- **B-UNKNOWN-DELETE**: Iteration 1 case 9 (Manual test)
- **B-UNKNOWN-DONE**: Iteration 1 case 8 (Manual test)
- **B-WHITESPACE**: Iteration 1 case 3 (Manual test)

## Limitations

- Discovery stages are assigned metadata, not inferred from execution.
- The invalid-ID case simulates the server's integer conversion boundary.
- HTML escaping requires a browser/UI test; this script only tests title storage.
- Missing edit/filter methods are reported as outstanding features.
