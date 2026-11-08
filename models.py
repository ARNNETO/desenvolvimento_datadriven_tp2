# from pydantic import BaseModel, Field
# from datetime import date


# class UserText(BaseModel):
#     text: str

# class UserTextTranslate(BaseModel):
#     text: str

# Importa bibliotecas
import torch
from transformers import (
                    pipeline, 
                    GenerationConfig, 
                    AutoModelForSeq2SeqLM, 
                    MarianTokenizer
                )
from langchain_core.language_models.fake import FakeListLLM
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from pathlib import Path

device = torch.device(
"cuda" if torch.cuda.is_available() else "cpu"
)


# Função para gerar texto usando o modelo openai-community/gpt2
pipe = pipeline(
"text-generation",
model="openai-community/gpt2",
dtype=torch.float32,
device=device,
clean_up_tokenization_spaces=False,
)
generation_config = GenerationConfig(
    max_new_tokens=50,
    do_sample=True,
    temperature=1.0,
    top_k=1000,
    top_p=0.1
)

def generate_text(text: str) -> str:
    prompt = text
    resultado = pipe(
        prompt,
        generation_config=generation_config,
        return_full_text=True,
    )
    return resultado[0]["generated_text"]

# Função para traduzir texto do ingês para o frances usando o modelo Helsinki-NLP/opus-mt-en-fr
translation_model_id = "Helsinki-NLP/opus-mt-en-fr"

translation_tokenizer = MarianTokenizer.from_pretrained(translation_model_id)
translation_model = AutoModelForSeq2SeqLM.from_pretrained(
    translation_model_id,
    dtype=torch.float32,
).to(device)
translation_model.eval()

@torch.inference_mode()
def translate_text(text: str) -> str:
    inputs = translation_tokenizer(text, return_tensors="pt").to(device)
    translated_ids = translation_model.generate(**inputs)
    return translation_tokenizer.decode(
        translated_ids[0],
        skip_special_tokens=True,
    )

# Função para executar FakeLLM simples
question_response = {
    "Olá. Tudo bem?": "Oie. Tudo bem sim. E contigo?",
    "O que é python?": "Python é uma linguagem de programação.",
    "O que é LLM": "Grande Modelo de Linguagem"
}

def simple_fakeLLM(text: str) -> str:
    resposta_predefinida = question_response.get(
        text,
        "Não tenho uma resposta para essa pergunta."
    )

    fake_llm = FakeListLLM(responses=[resposta_predefinida])

    resposta = fake_llm.invoke(text)
    return resposta

# Função tradutor usando Gpt e LangChain
load_dotenv()

modelo = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    api_key=os.environ["tradutor_api"],
)

def translate_openai(text: str) -> str: 
  prompt = ChatPromptTemplate.from_messages([
      (
          "system",
          "Traduza o texto recebido do inglês para o francês. "
          "Retorne somente a tradução, sem explicações. "
      ),
      ("human", "{text}"),
  ])

  chain = prompt | modelo

  resposta = chain.invoke({"text": text})
  return resposta.content
