# from langchain_core.prompts import PromptTemplate

# prompt = PromptTemplate.from_template(
#     "Explique {assunto} de forma resumida"
# )

# tema = "redes neurais"
# texto = prompt.format(assunto=tema)

# print(texto)

# from langchain_core.language_models.fake import FakeListLLM
# fake_llm = FakeListLLM(
#   responses = ["Olá, mundo"])

# resposta =fake_llm.invoke("")
# print(resposta)

# from langchain_core.prompts import PromptTemplate
# from langchain_core.language_models.fake import FakeListLLM

# fake_llm = FakeListLLM(
#   responses=["Olá!"]
# )

# prompt = PromptTemplate.from_template(
#   "Explique {assunto} de forma resumida."
# )

# chain = prompt | fake_llm
# resposta = chain.invoke({"assunto":"programação"})
# print(resposta)

from pathlib import Path

teste = Path().resolve().parent.parent.parent
print(teste)