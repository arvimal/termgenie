# TermGenie
#
import os
import sys
from openai import OpenAI
from rich.console import Console
import tomllib
import pathlib

# Fetch configuration
base_dir = pathlib.Path(__file__).parent
config_path = base_dir / "config.toml"
with open(config_path, "rb") as f:
    config = tomllib.load(f)

model = config["openai"]["model"]
temperature = config["openai"]["temperature"]
system_prompt = config["openai"]["messages"]["system_prompt"]

console = Console()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_AI(prompt):
    """
    Send the prompt to the AI API endpoint
    Get a response from the AI
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        console.print(f"[bold red] Enter your question or command: [/bold red]")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])
    console.print(f"[bold green] You: [/bold green]")

    reply = ask_AI(prompt)
    console.print(f"[bold blue] AI: [/bold blue]")
