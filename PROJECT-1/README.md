# 🧠 Project 1: AI Chatbot with Calculator Tool (LangChain)

This project is a simple terminal-based AI assistant powered by OpenAI and LangChain. It includes a custom tool that performs arithmetic operations and streams real-time responses like a terminal chatbot.

## 🛠 Features

- Chat with the AI assistant.
- Perform addition of two numbers using a custom tool.
- ReAct agent pattern with streaming output.
- Run in the terminal like a real Bash app.

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/aditya452007/3-BEGINNER-AI-PROJECT.git
cd 3-BEGINNER-AI-PROJECT/project-1

# Setup virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key to .env
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Run the chatbot
python main.py
