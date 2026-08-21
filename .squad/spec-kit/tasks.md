# Rock-Paper-Scissors CLI — tasks.md

Implementer: create runnable CLI and add score counters
- Acceptance:
  - src/rps.py exists and is executable (python3 src/rps.py runs).
  - Implements prompts, input normalization, random computer choice, outcome logic, and play-again loop exactly per specify.md.
  - Implements three in-memory counters initialized to zero on program start: player wins (You), computer wins (Computer), ties (Ties).
  - After each round result is printed, prints the exact single-line score summary:
    "Score - You: X Computer: Y Ties: Z"
    where X, Y, Z are integers reflecting current counts.
  - All original prompt and error message strings remain verbatim and unchanged.

Implementer: implement input validation and re-prompting
- Acceptance: invalid move and invalid play-again responses produce specified error messages and re-prompt until valid input is provided.

Implementer: implement outcome evaluation (win/lose/tie) and counter updates
- Acceptance:
  - For all 9 combinations of player vs computer, the printed "Result: ..." matches rock-paper-scissors rules.
  - Counters increment correctly after each round:
    - Player win => increment You
    - Computer win => increment Computer
    - Tie => increment Ties
  - The score line reflects the increments immediately and uses exact formatting.

Implementer: add minimal README run instruction (one-line)
- Acceptance: README.md (project root) contains one line: "Run: python3 src/rps.py"

Implementer: commit changes
- Acceptance:
  - Make a single commit on branch squad/1-rps-poc (or update that branch).
  - Commit message references "Closes #1" if an issue exists.
  - Include Co-authored-by trailer:
    Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

Tester: run quick happy-path smoke test including score verification
- Acceptance:
  - Tester runs the three sample sessions in specify.md and confirms:
    - All prompts and error messages are verbatim as specified.
    - After each round, the "Score - You: X Computer: Y Ties: Z" line appears and shows correct counts for the session.
    - Starting a new program run shows counters reset to zero (e.g., first round score shows one updated count and zeros for others).
  - Tester reports pass/fail and any deviations.

Notes
- Tasks are ordered for execution. Implementer should start at the top and proceed down the list.
- Keep scope minimal: in-session counters only, no persistence or external state.
