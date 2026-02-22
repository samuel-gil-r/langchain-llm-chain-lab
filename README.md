# LangChain LLM Chain 

This project is the first lab in the RAG (Retrieval-Augmented Generation) series. The goal is to understand how a basic chain works in LangChain by connecting a prompt, a language model, and an output parser.

For this lab, I used **Groq** as the LLM provider (instead of OpenAI) because it offers free access to models like `llama-3.3-70b-versatile`, allowing anyone to run the project without needing a credit card.

---

## What does this project do?

The script does three simple things:

1. Creates a chain in LangChain with a prompt, a model, and a parser
2. Asks the model three questions about AI concepts
3. Prints the answers in the terminal

This is the chain architecture:
```
User question
       ↓
  ChatPromptTemplate   (provides context and formats the message)
       ↓
    ChatGroq LLM       (the model that generates the answer)
       ↓
  StrOutputParser      (converts the answer to plain text)
       ↓
  Console output
```

---

## Requirements

- Python 3.9 or higher
- A free account at [Groq](https://console.groq.com) to get your API key

---

## Installation and setup

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/langchain-llm-chain-lab.git
cd langchain-llm-chain-lab
```

**2. Create and activate a virtual environment:**
```bash
python -m venv venv
```

# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Create your `.env` file** in the project root with your Groq API key:
```
GROQ_API_KEY=your-key-here
```

To get your API key, go to [console.groq.com](https://console.groq.com), create a free account, and generate a new key from the dashboard.

---

## How to run
```bash
python src/main.py
```

---

## Example output

When you run the script, you'll see something like this in your terminal:
```
Question: What is LangChain and what is it used for?
Answer: LangChain is an open-source platform designed to facilitate
the development of applications based on artificial intelligence...
------------------------------------------------------------

Question: What is a large language model (LLM)?
Answer: A large language model is an artificial intelligence system
trained with huge amounts of text...
------------------------------------------------------------

Question: Explain what a prompt is in 2 sentences.
Answer: A prompt is the instruction or question you give to the model to guide
its answer. Its purpose is to steer the model toward the result you need.
------------------------------------------------------------
```
<img width="1600" height="841" alt="image" src="https://github.com/user-attachments/assets/b6e50ee6-8a44-409c-85f7-46b9616a43a5" />

---

## Project structure
```
langchain-llm-chain-lab/
├── src/
│   └── main.py        # Main code with the LangChain chain
├── .env               # Your API key 
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Technologies used

- [LangChain](https://python.langchain.com/) — framework for building applications with LLMs
- [Groq](https://console.groq.com/) — free language model provider
- [llama-3.3-70b-versatile](https://console.groq.com/docs/models) — the LLM model used
- [python-dotenv](https://pypi.org/project/python-dotenv/) — for handling environment variables

## AUTHOR
- Samuel Antonio Gil Romero
## Subject
- TDSE-Tecnología y Desarrollo de Sistemas Empresariales

