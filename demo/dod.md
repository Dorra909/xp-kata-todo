# Definition of Done (DoD)

## 1. Purpose
A feature is done when it meets its requirements, passes testing, and works correctly.

## 2. Completion Criteria
- [ ] Functional requirements are implemented.
- [ ] Empty and whitespace-only titles are rejected.
- [ ] Search is case-insensitive.
- [ ] Invalid and unknown IDs are handled safely.
- [ ] Task IDs remain stable after deletion.
- [ ] Task completion and statistics work correctly.
- [ ] Editing and filtering are implemented if required.
- [ ] Accents, special characters, and long titles are handled correctly.
- [ ] Automated tests pass.
- [ ] Normal flows and all 16 extra cases are tested.
- [ ] Actual results and defects are recorded in journal.md.
- [ ] No unresolved critical defects remain.
- [ ] The application launches and can be demonstrated.

## 3. Testing Evidence
- Automated test results from pytest.
- Results of the 16 extra test cases.
- Generated journal.md with actual outcomes.
- Defect descriptions, discovery stages, and resolution status.

## 4. Current Status
Iteration 2 passes its existing eight unit tests.
Additional verification is required for accent-insensitive search, editing,
filtering, and demo-server input validation.

The project is considered done only after the applicable criteria
have been verified.
