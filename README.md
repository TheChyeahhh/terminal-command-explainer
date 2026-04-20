# terminal-command-explainer

> Instantly explain any terminal command using AI — powered by Claude or OpenAI.

Never copy a command from Stack Overflow without understanding it again.

---

## What does this tool actually do?

**It explains terminal commands. It does NOT run them.**

You paste a command in as text — the AI tells you what it does, what every part means, whether it's safe, and if there's a better way to do it. Nothing on your computer is touched.

> Think of it like Google Translate — but for terminal commands. You're translating a command into plain English, not executing it.

---

## Demo

```bash
$ explain "rm -rf node_modules"
```

```
╭─ Command Explained  via Claude ───────────────────────────────╮
│                                                               │
│  What it does                                                 │
│  Recursively deletes the node_modules folder and everything   │
│  inside it, with no confirmation prompt.                      │
│                                                               │
│  Breakdown                                                    │
│  • rm          — remove files or directories                  │
│  • -r          — recursive (go inside folders too)            │
│  • -f          — force (no "are you sure?" prompt)            │
│  • node_modules — the folder being targeted                   │
│                                                               │
│  Risk Level                                                   │
│  CAUTION — permanently deletes files, no undo                 │
│                                                               │
│  Safer Alternative                                            │
│  npx rimraf node_modules                                      │
│                                                               │
╰───────────────────────────────────────────────────────────────╯
```

---

## Features

- Explains what a command does in plain English
- Breaks down every flag and argument
- Rates risk level: `SAFE` / `CAUTION` / `DANGEROUS`
- Suggests safer alternatives when they exist
- Supports **Claude** (default) and **OpenAI** backends
- Clean, readable terminal output

---

## Complete Beginner Setup (Step by Step)

### Step 1 — Make sure you have Python installed

Open your terminal and run:

```bash
python3 --version
```

You should see something like `Python 3.9.x` or higher. If not, download Python at [python.org](https://www.python.org/downloads/).

---

### Step 2 — Download this tool

```bash
git clone https://github.com/TheChyeahhh/terminal-command-explainer.git
cd terminal-command-explainer
```

---

### Step 3 — Create a virtual environment

This keeps the tool's dependencies isolated from the rest of your system (best practice):

```bash
python3 -m venv .venv
```

---

### Step 4 — Activate the virtual environment

**Mac / Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

You'll know it worked when your terminal prompt shows `(.venv)` at the start.

---

### Step 5 — Install the tool

```bash
pip install -e .
```

---

### Step 6 — Add your API key

Copy the example config file:

```bash
cp .env.example .env
```

Open the `.env` file (it may be hidden — press `Cmd + Shift + .` on Mac to show hidden files) and replace the placeholder with your real API key:

```env
ANTHROPIC_API_KEY=sk-ant-your-real-key-here
OPENAI_API_KEY=sk-your-real-key-here
AI_BACKEND=claude
```

- Get a Claude key at [console.anthropic.com](https://console.anthropic.com)
- Get an OpenAI key at [platform.openai.com](https://platform.openai.com)

> Your key stays on your machine inside `.env` — it is never shared or uploaded (the `.gitignore` blocks it).

---

### Step 7 — Run it

```bash
explain "any command you want to understand"
```

That's it. You're done.

---

## Everyday Usage

```bash
# Saw a scary command online? Check it before running it
explain "sudo rm -rf /tmp/*"

# Don't know what a flag does?
explain "ls -lah"

# Learning Docker?
explain "docker run -it --rm ubuntu bash"

# Confused by a Git command?
explain "git rebase -i HEAD~3"

# Use OpenAI instead of Claude
explain "chmod 755 script.sh" --backend openai
```

---

## Every time you come back (after closing terminal)

You need to re-activate the virtual environment each session:

```bash
cd terminal-command-explainer
source .venv/bin/activate   # Mac/Linux
explain "your command here"
```

---

## Output breakdown

Every response gives you 4 things:

| Section | What it tells you |
| --- | --- |
| **What it does** | Plain English summary of the command |
| **Breakdown** | Every word, flag, and argument explained |
| **Risk Level** | SAFE / CAUTION / DANGEROUS with a reason |
| **Safer Alternative** | A better approach if one exists |

---

## Requirements

- Python 3.9+
- A [Claude API key](https://console.anthropic.com) and/or [OpenAI API key](https://platform.openai.com)

---

## Future Ideas

- `--history` flag to save explained commands to a local log
- Shell alias auto-installer (`explain --install-alias`)
- VS Code extension wrapper
- Batch mode: explain multiple commands from a file
- `--risk-only` flag for quick safety checks in CI pipelines

---

## License

MIT
