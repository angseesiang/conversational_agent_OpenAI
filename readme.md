cd /srv
vim .env
OPENAI_API_KEY=MENTION_YOUR_OPENAI_API_KEY
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
python ./src/agent.py
pytest
