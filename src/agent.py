# src/agent.py
# Compatible with openai>=1.0.0
# Loads OPENAI_API_KEY from /src/.env automatically
# Usage:
#   python ./src/agent.py
#   echo "Hello" | python ./src/agent.py

import os
import sys
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI

# Try importing specific errors (may vary slightly by SDK version)
try:
    from openai import APIError, RateLimitError, AuthenticationError, BadRequestError, APITimeoutError
except Exception:  # fallback if errors not available in your version
    APIError = RateLimitError = AuthenticationError = BadRequestError = APITimeoutError = Exception

# --- Load environment variables from /src/.env ---
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# --- Defaults ---
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
DEFAULT_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))


class Agent:
    def __init__(self, model: str = DEFAULT_MODEL, temperature: float = DEFAULT_TEMPERATURE):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Add it to /src/.env like:\n"
                "  OPENAI_API_KEY=sk-...\n"
            )
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature

    def generate_response(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Send a single-turn prompt and return the assistant's reply text.
        """
        if not prompt or not prompt.strip():
            return ""

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
            )
            return resp.choices[0].message.content or ""
        except AuthenticationError as e:
            return f"[Auth error] {e}. Check your OPENAI_API_KEY."
        except RateLimitError as e:
            return f"[Rate limit] {e}. Try again later or reduce request frequency."
        except BadRequestError as e:
            return f"[Bad request] {e}"
        except APITimeoutError as e:
            return f"[Timeout] {e}. Consider retrying."
        except APIError as e:
            return f"[API error] {e}"
        except Exception as e:
            return f"[Unexpected error] {e}"


def _interactive_loop(agent: Agent) -> None:
    print(f"Model: {agent.model}  |  Temperature: {agent.temperature}")
    print("Type your prompt and press Enter. Ctrl+C to exit.\n")
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            reply = agent.generate_response(user_input)
            print(f"\nAssistant: {reply}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break


if __name__ == "__main__":
    try:
        agent = Agent()
    except RuntimeError as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)

    if not sys.stdin.isatty():
        # Non-interactive: read stdin once
        prompt = sys.stdin.read()
        print(agent.generate_response(prompt))
    else:
        # Interactive loop
        _interactive_loop(agent)

