from openai import OpenAI
from typing import Any, Dict
import json

import os
from dotenv import load_dotenv

load_dotenv()

class ConversationalAgent:
    """A class to represent a conversational agent using OpenAI API."""

    def __init__(self, api_key: str):
        """
        Initialize the conversational agent with the given API key.

        Parameters:
        api_key (str): The API key to access OpenAI API.
        """
        self.api_key = api_key
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_response(self, user_input: str) -> str:
        """
        Generate a response based on the user input using OpenAI API.

        Parameters:
        user_input (str): The input from the user.

        Returns:
        str: The generated response from the agent.
        """
        try:
            response = self.client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": user_input},
                        ],
                        }
                    ],
                    max_tokens=150
                )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def process_parameters(parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process parameters provided in JSON format.

        Parameters:
        parameters (Dict[str, Any]): Parameters in JSON format.

        Returns:
        Dict[str, Any]: Processed parameters.
        """
        # Ensure parameters are in the correct format and types
        processed_params = {key: str(value) for key, value in parameters.items()}
        return processed_params

# Example usage
if __name__ == "__main__":
    agent = ConversationalAgent(api_key=os.getenv("OPENAI_API_KEY"))
    user_input = "Tell me a joke."
    print(agent.generate_response(user_input))
