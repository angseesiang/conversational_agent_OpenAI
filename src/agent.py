# src/agent.py
# Compatible with openai>=1.0.0
# Loads OPENAI_API_KEY from ./src/.env (or environment)

import os
from typing import Optional, Dict, Any

from dotenv import load_dotenv
from openai import OpenAI

try:
    from openai import APIError, RateLimitError, AuthenticationError, BadRequestError, APITimeoutError
except Exception:
    APIError = RateLimitError = AuthenticationError = BadRequestError = APITimeoutError = Exception

# Load env next to this file (fallback to process env)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
DEFAULT_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))

class ConversationalAgent:
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = DEFAULT_MODEL,
        temperature: float = DEFAULT_TEMPERATURE,
    ):
        key = api_key or os.getenv("OPENAI_API_KEY")
        if not key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Add it to src/.env or pass api_key to ConversationalAgent()."
            )
        self.client = OpenAI(api_key=key)
        self.model = model
        self.temperature = temperature

    def generate_response(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate a response from the OpenAI Chat API."""
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
            return f"[Rate limit] {e}."
        except BadRequestError as e:
            return f"[Bad request] {e}"
        except APITimeoutError as e:
            return f"[Timeout] {e}"
        except APIError as e:
            return f"[API error] {e}"
        except Exception as e:
            return f"[Unexpected error] {e}"

    @staticmethod
    def process_parameters(parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process parameters for testing compatibility.
        Currently just returns the dict unchanged.
        """
        return parameters

