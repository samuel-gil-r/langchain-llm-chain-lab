# LangChain LLM Chain - Lab 1

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

---

## Project structure
```
langchain-llm-chain-lab/
├── src/
│   └── main.py        # Main code with the LangChain chain
├── .env               # Your API key (not uploaded to GitHub)
├── .env.example       # Example .env file without real keys
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
- TDSE

# En Mac/Linux:
source venv/bin/activate

# En Windows:
venv\Scripts\activate
```

**3. Instala las dependencias:**
```bash
pip install -r requirements.txt
```

**4. Crea tu archivo `.env`** en la raíz del proyecto con tu API key de Groq:
```
GROQ_API_KEY=tu-clave-aqui
```

Para obtener tu API key ve a [console.groq.com](https://console.groq.com), crea una cuenta gratis y genera una nueva key desde el panel.

---

## Cómo ejecutarlo
```bash
python src/main.py
```

---

## Ejemplo de salida

Cuando ejecutas el script verás algo así en tu terminal:
```
Pregunta: ¿Qué es LangChain y para qué sirve?
Respuesta: LangChain es una plataforma de código abierto diseñada para facilitar
el desarrollo de aplicaciones basadas en inteligencia artificial...
------------------------------------------------------------

Pregunta: ¿Qué es un modelo de lenguaje grande (LLM)?
Respuesta: Un modelo de lenguaje grande es un sistema de inteligencia artificial
entrenado con enormes cantidades de texto...
------------------------------------------------------------

Pregunta: Explica qué es un prompt en 2 oraciones.
Respuesta: Un prompt es la instrucción o pregunta que le das al modelo para guiar
su respuesta. Su objetivo es orientar al modelo hacia el resultado que necesitas.
------------------------------------------------------------
```

---

## Estructura del proyecto
```
langchain-llm-chain-lab/
├── src/
│   └── main.py        # Código principal con la cadena LangChain
├── .env               # Tu API key (no se sube a GitHub)
├── .env.example       # Ejemplo del archivo .env sin claves reales
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Tecnologías usadas

- [LangChain](https://python.langchain.com/) — framework para construir aplicaciones con LLMs
- [Groq](https://console.groq.com/) — proveedor gratuito del modelo de lenguaje
- [llama-3.3-70b-versatile](https://console.groq.com/docs/models) — el modelo LLM usado
- [python-dotenv](https://pypi.org/project/python-dotenv/) — para manejar variables de entorno

## AUTOR
- Samuel Antonio GIl Romero
## Materia 
- TDSE 