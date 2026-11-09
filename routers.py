# Importa bibliotecas
from fastapi import APIRouter, HTTPException
# from models import UserText, UserTextTranslate
# from llm import generate_text
from models import (generate_text, translate_text,
                    simple_fakeLLM, translate_openai,
                    translate_helsinki
                )

router = APIRouter()

################################### PARTE 1 ###################################
# ------------------------------------------------------------------------------
# Questão 1
# ------------------------------------------------------------------------------
@router.post("/text-generation")
def text_generation(text: str):
    generated_text = generate_text(text)
    return { generated_text}

# ------------------------------------------------------------------------------
# Questão 2
# ------------------------------------------------------------------------------
@router.post("/text-translator")
def text_translator(text: str):
    translated_text = translate_text(text)
    return {translated_text}

################################### PARTE 2 ###################################
# ------------------------------------------------------------------------------
# Questão 1
# ------------------------------------------------------------------------------
@router.post("/simple-fakellm")
def fakellm(text: str):
    fakellm_text = simple_fakeLLM(text)
    return {fakellm_text}

# ------------------------------------------------------------------------------
# Questão 2
# ------------------------------------------------------------------------------
@router.post("/translate-openai")
def rota_translate_openai(text: str):
    translated_text = translate_openai(text)
    return {"traducao": translated_text}

# ------------------------------------------------------------------------------
# Questão 3
# ------------------------------------------------------------------------------
@router.post("/translate-helsinki")
def rota_translate_helsinki (text: str):
    translated_text = translate_helsinki(text)
    return {translated_text}
