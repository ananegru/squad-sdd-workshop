# Spec-Kit Constitution — Rock-Paper-Scissors CLI PoC

Owner: SpecKit (Spec-Kit Expert)
Created: 2026-08-14T11:53:07+02:00

Purpose:
- Define the minimal scope and acceptance criteria for the interactive Rock-Paper-Scissors (RPS) CLI PoC.
- Prioritize a runnable demo and the happy path only; no production concerns.

Scope:
- Single-player CLI where a human plays Rock, Paper, or Scissors against the computer.
- Interaction via standard input/output.
- Core happy path: user inputs a valid choice, computer picks, result computed, result shown, option to play again.
- No persistent state, no networking, no GUI.

Acceptance Criteria:
- The CLI starts with a prompt describing valid choices.
- The app accepts user input (case-insensitive) for rock, paper, scissors (or r/p/s), validates it, then shows the computer's choice and round result (win/lose/tie).
- Option to play another round or exit.
- When run, the happy path (valid user input) completes end-to-end without errors.

Artifacts required from SpecKit before planning:
1. specify.md — precise input/output examples and edge-case notes (only if needed); clarify only if ambiguity exists.
2. plan.md — minimal plan derived from specify (Planner uses Claude Opus 4.8 to produce tasks).
3. tasks.md — explicit tasks the Implementer will execute; each task has one-line acceptance criteria.

Notes:
- Testing limited to a quick happy-path smoke test by Tester.
- Timebox: keep work short; ship demo quickly.
