# TermGenie
#
import os
import sys
from openai import OpenAI 
from rich.console import Console 
import tomllib

# Fetch configuration
with open("config.toml", "rb") as f:
    config = tomllib.load(f)

model = config["openai"]["model"]
temperature = config["openai"]["temperature"]
system_prompt = config["openai.messages"]["system_prompt"]

console = Console()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_AI(prompt):
    """
    Send the prompt to the AI API endpoint
    Get a response from the AI
    """
    response = client.chat.completions.create()
