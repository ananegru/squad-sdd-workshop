# The Walkthrough: Spec Kit & Squad, Step by Step

Follow these steps in order. By the end you'll have built a Rock-Paper-Scissors CLI
game in Python, entirely from a spec, with a team of AI agents you assembled yourself.

### How to read this guide

| Marker | Where you type it |
|---|---|
| 🖥️ **Terminal** | Your shell (the Codespaces terminal) |
| 💬 **Squad** | Inside the running Copilot session (Steps 6+) |

Copy-paste the blocks as-is. After most commands there's a short **"What this does"**
so you can follow *why*, not just *what*; and if you're facilitating, so you can
narrate it out loud.

> Commands are shown for **bash** (Codespaces default). Where Windows PowerShell
> differs, a separate block is provided.

---

# Phase 1 · Set up your environment (Steps 1–5)

## Step 1: Update Copilot in Github Codespaces to the latest version

These tools change weekly, so start on the newest Copilot. 🖥️ **Terminal:**

```bash
curl -fsSL https://gh.io/copilot-install | sudo bash
```

**What this does:** downloads and installs the latest GitHub Copilot CLI. Run it even
if Copilot is already installed, it upgrades you to the current release so the rest of
the workshop behaves as described.

> Already inside a Copilot session? You can also just type `/update`.

---

## Step 2: Install Squad

🖥️ **Terminal:**

```bash
npm install -g @bradygaster/squad-cli
```

**What this does:** installs the **Squad CLI** globally. Squad is the framework that
lets you stand up a team of role-based AI agents in any repository. Confirm it landed:

```bash
squad --version
```

---

## Step 3: Initialize Squad in your project

Move into the folder you want to build in (create one if needed), then initialize:

```bash
squad init
```

**What this does:** scaffolds Squad into the current folder. It:

- creates the **coordinator**, the agent that routes work and enforces the rules,
  defined at `.github/agents/squad.agent.md`;
- creates the **`.squad/` team-state directory**, where every agent, charter, routing
  rule, and decision will live;
- registers **4 built-in background agents** that come with every Squad:

| Built-in agent | Role |
|---|---|
| **scribe** | Session logger & memory: records what happened |
| **ralph** | Work monitor: watches the queue and phase gates |
| **rai** | Responsible-AI reviewer: safety, bias, secrets |
| **fact-checker** | Devil's advocate: verifies claims, challenges assumptions |

> **You may be asked to add `@copilot` to your roster.** That's Squad offering to
> include the Copilot coding agent as a teammate. Accept it to let Copilot pick up
> issues later. 

These four are *functional roles with fixed names*. They're always present. The
**themed** teammates (the planner, spec expert, implementer, tester…) don't exist yet;
**you'll cast them in Step 6.**

---

## Step 4: Install `uv`

`uv` is a fast Python package/environment manager. Spec Kit runs through it, and it'll
run your game later. 🖥️ **Terminal:**

**macOS / Linux (bash):**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**What this does:** installs `uv`. You may need to open a new terminal (or run the
"source" line the installer prints) so `uv` is on your `PATH`. Confirm:

```bash
uv --version
```

---

## Step 5: Initialize Spec Kit

Now bring in **Spec Kit**, the spec-driven workflow. Install its CLI (using the `uv`
from Step 4), then initialize it **in your current project folder**, the same folder
where you ran `squad init`. 🖥️ **Terminal:**

```bash
uv tool install specify-cli
specify init .
```

`specify init` then asks two questions. Answer:

- **Which agent?** → choose **`copilot`**
- **Which script type?** → choose **`sh` (bash)** _(on Windows, choose `ps`)_

> **Prefer no prompts?** Pass the answers as flags:
> `specify init . --integration copilot --script sh`
> **Don't want to install the CLI?** Run it one-off with `uv`:
> `uvx --from git+https://github.com/github/spec-kit.git specify init .`

**What this does:** wires Spec Kit into your repo for Copilot: it writes the workflow
prompts under `.github/` and its templates, scripts, and memory under `.specify/`.
After this, commands like `/speckit.constitution`, `/speckit.specify`, `/speckit.plan`,
`/speckit.tasks`, and `/speckit.implement` are available inside Copilot. **You won't run
these by hand**: your Squad's spec expert drives them for you in Phase 3.

**Environment check.** You should now have four things working: the latest
`copilot`, `squad`, `uv`, and Spec Kit initialized in your repo.

---

# Phase 2 · Assemble your Squad (Steps 6–7)

## Step 6: Launch the Squad and cast your team

Start an interactive Copilot session **as the Squad coordinator**. 🖥️ **Terminal:**

```bash
copilot --agent squad
```

Once inside, pick your model. 💬 **Squad** (type the slash command):

```text
/model
```

Select **Claude Opus 4.8** and set reasoning effort to **Extra High**. This is the
coordinator's brain for the session. You want its best reasoning while it designs the
team.

> **You may see a `git config user.name` prompt.** Squad reads and prints the name in
> your Git config (the identity attached to your commits) so it knows who owns the
> project. Confirm it or set one with `git config --global user.name "Your Name"`.

Now cast the team. 💬 **Squad**, paste this entire prompt:

```text
Create a squad optimized for shipping proof-of-concept apps fast; this team does not build for production, so it should prioritize speed and a working demo over robustness, scale, or polish. Its first objective is to build an interactive Rock-Paper-Scissors CLI app in Python. Spec-kit is mandatory and no work happens outside of it: the squad has one dedicated spec-kit expert who owns the spec-kit workflow and drives it from constitution to specify to plan to tasks to implement, using clarify only when a spec is genuinely ambiguous and skipping analyze, while the rest of the team follows the artifacts this expert produces and never skips ahead, meaning no planning before specs exist and no code before tasks exist. The definition of done is simply that the app runs and the happy path works end-to-end, with no gold-plating. The tester should run only a quick happy-path smoke test rather than testing edge cases or chasing coverage, verifying quickly that it works and then moving on to the next build. For models, use Claude Opus 4.8 for the planner and spec-kit expert, since it's the most capable at deep reasoning and architecture where mistakes cost the most; Claude Sonnet 4.6 for the implementer, since it balances strong coding with speed and cost for high-volume work; and Claude Haiku 4.5 for the coordinator and admin, since it's the fastest and cheapest for lightweight, routine tasks.
```

**What this does:** this one prompt encodes your whole team design: its *goal* (fast
proof-of-concept), its *process* (Spec Kit is mandatory, phase-gated, with a dedicated
spec-kit owner), its *definition of done* (happy path runs), and a *model per role*
(the expensive, capable model where reasoning matters; the cheap, fast one for routine
work). The coordinator reads it and proposes a **roster**, a set of named teammates
with charters and models.

> **The names will surprise you.** Squad "casts" themed agents from a fictional
> *universe* (a movie, show, etc.), so your spec expert might be called *Mikey* and
> your implementer *Brand*. The **names differ every run**: what matters is the
> **role** each one plays. The 4 built-ins from Step 3 keep their fixed names.

---

## Step 7: Accept the team and tour what it created

Review the proposed roster, then approve it. 💬 **Squad:**

```text
Looks good, create the team.
```

**What this does:** Squad writes the whole team to disk. This is the moment to slow
down and **open the files it just created**. The entire team is plain text you can
read. Here's the tour, and what each file is for:

| File | What it is |
|---|---|
| `.squad/config.json` | **Per-agent model config.** Maps each teammate to the model you chose (e.g. planner → Claude Opus 4.8). Also records the state backend. |
| `.squad/casting/registry.json` | **The authoritative roster**: the current source of truth for *who is on the team*, their role → name, and whether they're active. |
| `.squad/casting/history.json` | **The casting audit trail.** Records which universe was used and a snapshot of each casting decision (which role got which name/identity, and when), the team's bookkeeping/memory over time. |
| `.squad/agents/<name>/charter.md` | **Each teammate's charter**: who they are, what they own, their boundaries, their model, and their voice. This is the agent's identity. |
| `.squad/agents/<name>/history.md` | **Each teammate's private history**, a fresh log per agent that grows over time: decisions made, work completed, and learnings, stamped with dates. |
| `.squad/routing.md` | **The routing rules**: a table dictating who handles what kind of work. |
| `.squad/decisions.md` | **Durable team decisions**: the rules and directives every agent must respect (e.g. "Spec Kit is authoritative; no code before tasks"). |
| `.squad/team.md` | **The full roster page**: the coordinator plus every member (themed *and* built-in) in one readable table. |

🖥️ **Terminal**, open a few to see for yourself (in a second terminal, or after you
`/exit`):

```bash
cat .squad/team.md
cat .squad/casting/registry.json
cat .squad/agents/*/charter.md
```

**Two things worth pointing out while you read:**

- **Why the registry only lists *some* agents.** `registry.json` shows only the
  **themed** teammates you cast. The built-ins (scribe, ralph, rai, fact-checker)
  aren't there because they're fixed-name functional roles; they're never "cast" from
  a universe, so they don't need a casting record. (They still appear in `team.md`.)
- **Registry vs. history.** The **registry** answers *"who's on the team right now?"*
  quickly; the **history** preserves the full casting audit trail. Keeping them
  separate lets Squad look up the current roster fast while never losing the record of
  how the team was built. `history.md` files keep growing as the team works: new
  agents, charter edits, and completed work all get logged.

### Two quick things to note as you build

**a) See the team working: `/tasks`.** 💬 **Squad:**

```text
/tasks
```

**What this does:** shows the subagents and shell commands currently running. As the
team fans out in Phase 3, this is where you watch individual agents pick up work in
parallel.

**b) Auto-approve tools for the workshop: `/allow-all`.** 💬 **Squad:**

```text
/allow-all
```

**What this does:** enables all permissions (tools, file paths, and URLs) so the team
can work without stopping to ask you to approve every action. Handy for a fast
workshop. Outside a workshop, leave approvals on so you stay in the loop.

---

# Phase 3 · Build & run the game (Steps 8–9)

## Step 8: Let the team build the game from the spec

Here's the payoff of everything so far: your spec expert now drives the **full Spec Kit
workflow** before a single line of game code is written.

Often **the coordinator offers to start on its own**. If it asks *"shall I begin the
Spec Kit workflow?"*, say yes. If it doesn't, nudge it. 💬 **Squad:**

```text
Begin the build. Have the spec-kit expert drive the Spec Kit workflow end to end.
```

**What this does:** the spec expert works through the phases *in order*, producing an
artifact at each gate. You'll see it move through:

`constitution` → `specify` → *(clarify only if ambiguous)* → `plan` → `tasks` → `implement`

The spec artifacts get written under `specs/<NNN-rock-paper-scissors>/` (with the
constitution under `.specify/memory/`). The rest of the team stays gated: no plan
before the spec, no code before tasks.

**Before it writes code, review the spec.** This is the heart of spec-driven
development. You inspect intent *before* implementation. You could ask squad something like: 💬 **Squad:**

```text
Spec-kit expert: review the current spec against Spec Kit standards and against our objective: a very simple, interactive, CLI-based Rock-Paper-Scissors game. Point out anything ambiguous, missing, or over-scoped, and suggest improvements before we implement.
```

**What this does:** asks the spec owner to sanity-check its own spec for clarity,
completeness, and scope creep, and to tighten it *before* code locks the behavior in.

**Now make the spec simpler.** A first spec almost always carries more than a quick
demo needs. Having just read it, push it back toward the minimum. 💬 **Squad:**

```text
After seeing the spec, make it simpler.
```

**What this does:** turns your review into action. Instead of only noting scope creep,
you have the spec owner trim the spec to its essentials, matching the "no gold-plating"
definition of done you set in Step 6. Because the plan and tasks are generated *from*
the spec, cutting scope here keeps the entire downstream chain lean.

When you're happy, let the team proceed to `implement`. 💬 **Squad:**

```text
Looks good, proceed to implement.
```

Watch the implementer write the game and the tester run a quick happy-path smoke test,
exactly as your Step 6 design specified.

> **If the team stalls or drifts:** the spec is the contract, not the chatter. Point it
> back at a specific requirement, or narrow the request to one task, and continue.

---

## Step 9: Run the game

Ask the team how to run it. It knows how it built the app. 💬 **Squad:**

```text
How do I run the game?
```

Then run whatever it tells you. It's typically one line. 🖥️ **Terminal** (example):

```bash
uv run python main.py
```

_(If it built a plain script, `python3 main.py` may be all you need. Follow the
team's instructions.)_

**What this does:** launches your Rock-Paper-Scissors game. Play a few rounds: enter
`rock`, `paper`, or `scissors`, watch the computer play and the score update, then quit.
 **You built a working app from a spec, with a team you assembled.**

---

# Phase 4 · Extend the project (Steps 10–11)

The point of a spec + team is that *changes* follow the same disciplined path. Let's
prove it twice.

## Step 10: Add a new feature (a score counter)

Back in the Squad session, ask for the feature, and require it to go through Spec Kit
like everything else. 💬 **Squad:**

```text
Add a very simple score counter. Run it through Spec Kit the same way: specify the feature, update the plan and tasks, then implement.
```

**What this does:** kicks off a **new Spec Kit cycle** scoped to just this feature. The
spec expert specifies the score-counter behavior, updates the plan/tasks, and only then
does the implementer touch code: no shortcut straight to the keyboard. When it's done,
run the game again (Step 9) and confirm the score now persists across rounds.

> **Notice the discipline:** even a tiny feature starts with a spec change. That's SDD:
> intent leads, code follows.

---

## Step 11: Add a new role to the team (a Scrum Master)

Finally, grow the *team* itself. Ask Squad to cast a brand-new role. 💬 **Squad:**

```text
Let's add a role to the team - a scrum master. He will be responsible for doing retrospectives on demand. He will focus on analyzing GitHub Copilot logs and squad logs and based on the information found, he would propose improvements for our team members that we would add to their charters.
```

**What this does:** Squad **casts a new agent** into your existing team, same as Step
6, but for one role. Watch it update the very files you toured in Step 7:

- a new **`.squad/agents/<scrum-master-name>/charter.md`** and **`history.md`** appear;
- **`casting/registry.json`** and **`casting/history.json`** record the new cast member;
- **`team.md`** and **`routing.md`** update so the coordinator knows the role exists and
  what to route to it;
- relevant **`decisions.md`** entries may be added.

Then try the role out. 💬 **Squad:**

```text
Scrum master: run a quick retrospective on this session and propose one improvement for each teammate's charter.
```

**What this does:** exercises your new agent immediately: it reviews the session logs
and proposes charter improvements, closing the loop on a team that can **inspect and
improve itself.**

---

## Wrap-up

In about an hour you went from an empty folder to:

- a **working Rock-Paper-Scissors game** in Python that you never hand-coded;
- a full **Spec Kit artifact chain** (constitution → spec → plan → tasks) that governed
  every change;
- a **Squad** of role-based agents (cast, extended, and self-reviewing) all stored as
  plain, inspectable files in your repo.

**What you practiced:**

| Habit | Where you saw it |
|---|---|
| Spec before code | Step 8: no implementation until tasks existed |
| Phase-gated workflow | The spec expert moving constitution → … → implement in order |
| Role-based routing | `routing.md` sending work to the right teammate |
| Model tiers | `config.json`: capable model for reasoning, cheap model for routine work |
| Changes follow the spec | Step 10: a new feature started with a spec change |
| A team that evolves | Step 11: casting a new role and having it improve the team |

### Where to go next

- Add another feature (best-of-5 rounds, a "quit" summary): again, spec first.
- Open `.squad/decisions.md` after a few changes and watch the team's memory grow.
- Reuse this flow in your own repo with your own product idea.

> **Remember:** Squad and Spec Kit evolve fast. If a command name, flag, or file
> location differs from this guide, trust the live tool (`squad --help`,
> `specify --help`, and Copilot's `/help`): the *spec-first, team-implements* flow is
> what matters.
