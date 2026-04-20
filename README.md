# terminal-command-explainer

> Instantly explain any terminal command using AI — powered by Claude or OpenAI.

Never copy a command from Stack Overflow without understanding it again.

---

## Demo

```bash
$ explain "rm -rf node_modules"
```

```
╭─ Command Explained  via Claude ──────────────────────────────╮
│                                                               │
│  ## What it does                                              │
│  Recursively deletes the node_modules directory and all of   │
│  its contents without asking for confirmation.               │
│                                                               │
│  ## Breakdown                                                 │
│  - rm     — remove files or directories                       │
│  - -r     — recursive (delete directory contents)            │
│  - -f     — force (no confirmation prompts)                   │
│  - node_modules — the target directory                        │
│                                                               │
│  ## Risk Level                                                │
│  CAUTION — permanently deletes files, no undo                 │
│                                                               │
│  ## Safer Alternative                                         │
│  Move to trash instead: `trash node_modules`                  │
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
- Clean, readable terminal output via `rich`

---

## Installation

```bash
git clone https://github.com/TheChyeahhh/terminal-command-explainer.git
cd terminal-command-explainer
pip install -e .
```

---

## Setup

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```env
ANTHROPIC_API_KEY=your_key_here   # get at console.anthropic.com
OPENAI_API_KEY=your_key_here      # get at platform.openai.com
AI_BACKEND=claude                  # or: openai
```

---

## Usage

```bash
# Explain a command (uses Claude by default)
explain "ls -la /etc"

# Use OpenAI instead
explain "curl -X POST https://api.example.com" --backend openai

# Short flag
explain "grep -r 'TODO' ." -b claude
```

---

## Examples

```bash
explain "chmod 755 script.sh"
explain "docker run -it --rm ubuntu bash"
explain "git rebase -i HEAD~3"
explain "lsof -i :8080"
explain "ps aux | grep python"
```

---

## Requirements

- Python 3.9+
- An [Anthropic API key](https://console.anthropic.com) and/or [OpenAI API key](https://platform.openai.com)

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
