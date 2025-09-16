# 🤖 Conversational Agent with OpenAI API

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](#)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green)](#)
[![Pytest](https://img.shields.io/badge/Tested-Pytest-orange)](#)

This project implements a **conversational agent** powered by the OpenAI API.  
It provides a simple Python interface for generating responses, processing parameters,  
and includes unit tests for validation.

---

## 📖 Contents

- `agent.py` – Core implementation of the conversational agent  
- `test_agent.py` – Unit tests for the agent  
- `.env` – Stores your **OpenAI API key**  
- `requirements.txt` – Project dependencies  
- `url.txt` – Repository reference  

---

## 🚀 How to Use

### 1) Clone this repository

```bash
git clone https://github.com/angseesiang/conversational_agent_OpenAI.git
cd conversational_agent_OpenAI
```

### 2) Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux / macOS
venv\Scripts\activate      # On Windows
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure your OpenAI API key

Create a `.env` file in the project root and add:

```env
OPENAI_API_KEY=your_api_key_here
```

### 5) Run the agent

```bash
python agent.py
```

You can interact with the agent directly or import the `ConversationalAgent` class in your own scripts.

### 6) Run unit tests

```bash
pytest test_agent.py
```

This will validate that the agent responds correctly and that parameter handling works.

---

## 🛠️ Requirements

- Python 3.9+  
- OpenAI  
- Pytest  
- Python-dotenv  

All dependencies are listed in `requirements.txt`.

---

## 📌 Notes

- The agent uses the **OpenAI GPT-4o** model by default.  
- Ensure your `.env` file contains a valid API key.  
- Unit tests validate both response generation and parameter handling.  

---

## 📜 License

This project is for **educational purposes only**.
