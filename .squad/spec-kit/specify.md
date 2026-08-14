# Rock-Paper-Scissors CLI — specify.md

Purpose
- Minimal, self-contained I/O specification for the single-player interactive CLI PoC.

Runtime behavior (required)
- On start, print a single-line prompt describing valid choices:
  "Choose [rock|paper|scissors] (or r/p/s):"
- Read one line of user input (stdin). Accept case-insensitive full words or single-letter shorthand:
  Valid inputs: rock, paper, scissors, r, p, s (any case).
- If input is valid, normalize to one of: rock, paper, scissors.
- Computer chooses uniformly at random from {rock, paper, scissors}.
- Print the computer choice and the round result as two lines:
  - "Computer chose: <choice>"
  - "Result: You win. / You lose. / Tie."
- Prompt the user to play again with:
  "Play again? (y/n):"
  Accept y/yes or n/no (case-insensitive). On 'y' repeat; on 'n' exit with zero status.
- If the user gives an invalid choice at either prompt, print a single-line error and re-prompt:
  - Invalid move: "Invalid choice. Please enter rock, paper, or scissors (r/p/s)."
  - Invalid play-again: "Invalid response. Enter y or n."

Input normalization and determinism
- Inputs are trimmed and lowercased before matching.
- The computer choice is non-deterministic (random). Tests should exercise functionality, not exact computer outputs.

Success criteria (happy path)
- For a valid user choice followed by a valid play-again decision, the program prints the computer choice and correct result and exits or repeats as requested without crashing.

Minimal edge handling (only what's needed)
- Invalid input => show error + re-prompt (no limit on retries).
- No persistence, no config, no networking.
- On EOF (e.g., Ctrl-D), exit gracefully with status 0.

Sample sessions (each block shows exact stdout then user input prefixed with ">")

1) User wins
CLI: Choose [rock|paper|scissors] (or r/p/s):
> rock
CLI: Computer chose: scissors
CLI: Result: You win.
CLI: Play again? (y/n):
> n
(program exits)

2) User loses
CLI: Choose [rock|paper|scissors] (or r/p/s):
> P
CLI: Computer chose: scissors
CLI: Result: You lose.
CLI: Play again? (y/n):
> n

3) Tie, then play again -> win
CLI: Choose [rock|paper|scissors] (or r/p/s):
> s
CLI: Computer chose: scissors
CLI: Result: Tie.
CLI: Play again? (y/n):
> y
CLI: Choose [rock|paper|scissors] (or r/p/s):
> paper
CLI: Computer chose: rock
CLI: Result: You win.
CLI: Play again? (y/n):
> n

Notes to Implementer
- Keep interaction exactly as specified (prompt lines and error messages) to make Tester expectations simple.
- Implementation may be in any language; produce a single executable script at src/rps.py and make it runnable (e.g., python3 src/rps.py) with no external dependencies.

No clarification needed.
