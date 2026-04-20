import os
import sys
import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.text import Text
from dotenv import load_dotenv

load_dotenv()
console = Console()

SYSTEM_PROMPT = """You are a terminal command expert. When given a shell command, respond in this exact format:

## What it does
A clear 1-3 sentence explanation of what the command does.

## Breakdown
A brief explanation of each flag, argument, or part of the command.

## Risk Level
One of: SAFE / CAUTION / DANGEROUS — with a one-line reason.

## Safer Alternative
If a safer or more modern alternative exists, show it. Otherwise write "None needed."

Be concise. No fluff. Developers are your audience."""


def get_claude_explanation(command: str) -> str:
    import anthropic
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set in environment.")
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"Explain this command: {command}"}],
    )
    return message.content[0].text


def get_openai_explanation(command: str) -> str:
    from openai import OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in environment.")
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Explain this command: {command}"},
        ],
        max_tokens=1024,
    )
    return response.choices[0].message.content


@click.command()
@click.argument("command")
@click.option(
    "--backend",
    "-b",
    default=None,
    type=click.Choice(["claude", "openai"], case_sensitive=False),
    help="AI backend to use (claude or openai). Defaults to AI_BACKEND env var or claude.",
)
def main(command: str, backend: str):
    """Explain any terminal command using AI.

    \b
    Examples:
      explain "rm -rf node_modules"
      explain "lsof -i :3000" --backend openai
      explain "git rebase -i HEAD~3"
    """
    selected = backend or os.getenv("AI_BACKEND", "claude").lower()

    console.print()
    console.print(Text(f"  $ {command}", style="bold cyan"))
    console.print()

    with console.status("[bold green]Analyzing command...[/bold green]"):
        try:
            if selected == "openai":
                result = get_openai_explanation(command)
                badge = "[dim]via OpenAI[/dim]"
            else:
                result = get_claude_explanation(command)
                badge = "[dim]via Claude[/dim]"
        except ValueError as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
            console.print(
                "[yellow]Tip:[/yellow] Copy [bold].env.example[/bold] to [bold].env[/bold] and add your API key."
            )
            sys.exit(1)
        except Exception as e:
            console.print(f"[bold red]Unexpected error:[/bold red] {e}")
            sys.exit(1)

    console.print(
        Panel(
            Markdown(result),
            title=f"[bold white]Command Explained[/bold white]  {badge}",
            border_style="cyan",
            padding=(1, 2),
        )
    )
    console.print()


if __name__ == "__main__":
    main()
