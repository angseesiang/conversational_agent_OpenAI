import pytest
from src.agent import ConversationalAgent

@pytest.fixture
def agent():
    return ConversationalAgent(api_key="your-api-key-here")

def test_generate_response(agent):
    user_input = "Tell me a joke."
    response = agent.generate_response(user_input)
    assert isinstance(response, str)
    assert len(response) > 0

def test_process_parameters():
    parameters = {"userInput": "Hello, world!"}
    processed = ConversationalAgent.process_parameters(parameters)
    assert processed == {"userInput": "Hello, world!"}

if __name__ == "__main__":
    pytest.main()
