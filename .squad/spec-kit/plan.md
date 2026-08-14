# Rock-Paper-Scissors CLI — plan.md

Objective
- Deliver a minimal interactive CLI PoC that satisfies the specify.md happy path and adds an in-session score counter showing You/Computer/Ties after every round.

Workstreams (time-boxed, minimal)
1. Implementation (core CLI + score)
   - Create/modify single-file CLI at src/rps.py implementing prompts, input normalization, random computer choice, outcome logic, play-again loop, error messages exactly as specified, and the in-session score counters (You wins, Computer wins, Ties) with the exact score line output: "Score - You: X Computer: Y Ties: Z".
   - Timebox: 1–2 hours.
2. Local verification (Implementer)
   - Run simple local runs to validate the sample sessions and correct score increments and formatting.
   - Timebox: 15–30 minutes.
3. Quick smoke test (Tester)
   - Run through the three sample sessions in specify.md and confirm score behavior and that all original prompt and message strings remain verbatim.
   - Timebox: 30 minutes.

Assumptions
- Single-file script is acceptable.
- Python 3 is available in the environment (recommended). If Implementer prefers another language, preserve CLI text and file location (src/rps.py can be replaced with an executable at the same path).
- No persistence, no config, no external services.
- Tests are manual smoke runs following sample sessions.

Rationale
- Adding a small in-session score counter keeps scope tiny while enhancing the PoC. Keeping all original phrasing verbatim makes acceptance straightforward.
