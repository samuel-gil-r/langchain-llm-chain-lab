import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def main():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente útil. Responde en español."),
        ("user", "{input}")
    ])

    chain = prompt | llm | StrOutputParser()

    preguntas = [
        "¿Qué es LangChain y para qué sirve?",
        "¿Qué es un modelo de lenguaje grande (LLM)?",
        "Explica qué es un prompt en 2 oraciones."
    ]

    for pregunta in preguntas:
        print(f"\nPregunta: {pregunta}")
        print(f"Respuesta: {chain.invoke({'input': pregunta})}")
        print("-" * 60)

if __name__ == "__main__":
    main()