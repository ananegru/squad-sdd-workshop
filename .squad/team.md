# Squad Team

> squad-sdd-workshop

Squad v0.12.0

💡 Say "squad commands" to see what I can do.

## Coordinator

| Name | Role | Notes |
|------|------|-------|
| Squad | Coordinator | Routes work, enforces handoffs and reviewer gates. Uses Claude Haiku 4.5 for lightweight coordination and admin tasks. |

## Members

| Name | Role | Charter | Status |
|------|------|---------|--------|
| SpecKit | Spec-Kit Expert | .squad/agents/spec-kit/charter.md | active |
| Planner | Planner (PoC) | .squad/agents/planner/charter.md | active |
| Implementer | Implementer (Python) | .squad/agents/implementer/charter.md | active |
| Tester | Tester (smoke) | .squad/agents/tester/charter.md | active |
| Scribe | Session Logger | .squad/agents/scribe/charter.md | active |
| Admin | Admin / Ops (lightweight) | .squad/agents/admin/charter.md | active |

## Coding Agent

<!-- copilot-auto-assign: false -->

| Name | Role | Charter | Status |
|------|------|---------|--------|
| @copilot | Coding Agent | — | 🤖 Coding Agent |

### Workflow Rules (PoC, Spec-Kit First)

- Spec-kit is MANDATORY. No planning or code work happens outside the spec-kit artifacts produced by SpecKit.
- SpecKit produces: constitution → specify → plan → tasks → implement. Skip analyze and use clarify only when a spec is genuinely ambiguous.
- Planner and SpecKit both use Claude Opus 4.8 (deep reasoning) for spec and planning decisions.
- Implementers use Claude Sonnet 4.6 for code generation (balance of speed and quality).
- Coordinator and Admin use Claude Haiku 4.5 for quick, cheap coordination and routine edits.
- Tester runs a quick happy-path smoke test only; verify that the happy path runs end-to-end and report pass/fail concisely.
- Definition of Done: the app runs and the happy path works end-to-end. No gold-plating.
- Branch naming convention: `squad/{issue-number}-{kebab-case-slug}` (use for issue-based work).

## Project Context

- **Project:** squad-sdd-workshop
- **First objective:** interactive Rock-Paper-Scissors CLI app in Python (PoC).
- **Created:** 2026-08-14

## Notes

- This squad is optimized for speed and demos; robustness, scale, and polish are intentionally deprioritized.
- All team members must follow the Spec-Kit Expert's artifacts and acceptance criteria; do not skip ahead.

