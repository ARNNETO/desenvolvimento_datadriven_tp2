# Importa bibliotecas
from fastapi import APIRouter, HTTPException
# from models import UserText, UserTextTranslate
# from llm import generate_text
from models import (generate_text, translate_text,
                    simple_fakeLLM, translate_openai
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

# ------------------------------------------------------------------------------
# Questão 3
# ------------------------------------------------------------------------------
'''
--> 1. Precisão da tradução: 
o modelo faz a tradução do inglês para o francês conforme ele foi criado, mas pode 
errar palavras de tuplo significado, termos técnicos e frases mais complexas. 
A tradução até pode ser fluída e pode atender tarefas simples, porém pode não trazer 
o significado real da frase ou texto. 

--> 2. Tempo de resposta e desempenho:
Textos longos e muitos acessos simultâneos aumentam consequentemente o tempo de 
processamento. Já a velocidade, isso depende do equipamento que está sendo utilizado. 
Se for um equipamento rubusto, logo a resposta será rápida. Caso seja utilizado um 
equipamento mais simples, consequentemente a resposta levará mais tempo.

--> 3. Custo e escalabilidade: 
Execução local não exige pagamento por tradução, mas consome memória e processamento
 do equipamento utilizado. Dependendo das configurações aplicadas no modelo, pode 
 aumenta a necessidade de memória, e atender mais requisições simultânias pode exigir 
 infraestrutura adicional.

--> 4. Gírias e contexto: 
Como é um modelo simples e como não há novos treinamentos, gírias, ironias e 
expressões idiomáticas, por exemplo, podem ser traduzidas de forma literal, não
interpretando de fato o que o texto original quer dizer.
'''

# ------------------------------------------------------------------------------
# Questão 4
# ------------------------------------------------------------------------------
'''
1. Coerência do texto: 
O modelo GPT-2 utilizado na questão 1 pode até gerar frases bem estruturadas, mas 
tende a perder o assunto em textos longos, repetir ideias e até mesmo apresentar 
contradições.

2. Falhas e incoerências: 
Devido sua obsolecência, o modelo pode inventar informações, confundir fatos e 
produzir respostas que até parecem corretas, mas não são. Seu funcionamento não 
garante que o conteúdo seja correto.

3. Desempenho e latência: 
Textos muito grandes e dependendo das configurações do modelo mais equipamentos 
com menos recursos tendem  a aumentar o tempo de resposta. Então, é necessário 
avaliar como seu uso será aplicado.

4. Conteúdo apropriado:
O modelo pode reproduzir preconceitos, linguagem ofensiva e informações inadequadas 
presentes nos dados de treinamento. O GPT-2 original não possui o mesmo treinamento 
para seguir instruções e evitar conteúdo prejudicial encontrado em modelos modernos.
'''

################################### PARTE 2 ###################################
# ------------------------------------------------------------------------------
# Questão 1
# ------------------------------------------------------------------------------
@router.post("/simple-fakellm")
def fakellm(text: str):
    fakellm_text = simple_fakeLLM(text)
    return {fakellm_text}

"""
Utilizar o fakeLLM permite testar o funcionamento da aplicação sem precisar utilizar 
um modelo real. Isso ajudar a ter respostas rápidas sem aguardar que um modelo real 
gere respostas e sem a necessidade de consumir tokens que são pagos.

                                            __________________________
                                            | Usuário insere pergunta| 
                                            __________________________

                                                        ⬇︎
                                            __________________________
                                            | Modelo recebe a pergunta| 
                                            __________________________

                                                        ⬇︎
_______________________                     __________________________
⏐  Seleciona resposta   ⏐   ⬅︎ Não  ⬅︎      ⏐    Pergunta existe?     ⏐
|       padrão          |                   __________________________
________________________          
                                                        ⬇︎
                ⏐                                      Sim
                ⏐                                       ⬇︎
                ⏐                           __________________________
                ⏐                           ⏐   Seleciona a resposta ⏐
                ⏐                           ⏐     correspondente     ⏐
                ⏐                           __________________________
                ⏐                                       ⬇︎
                ⏐                           __________________________
                ⏐-------------------------> ⏐   FakeListLLM recebe a ⏐
                                            ⏐ resposta selecionada   ⏐
                                            __________________________

                                                        ⬇︎
                                            __________________________
                                            ⏐     invoke retorna     ⏐
                                            ⏐       a resposta       ⏐
                                            __________________________

                                                        ⬇︎
                                            __________________________
                                            ⏐     FastAPI exibe a    ⏐
                                            ⏐   resposta aousuário   ⏐
                                            __________________________
                                            
"""

# ------------------------------------------------------------------------------
# Questão 2
# ------------------------------------------------------------------------------
@router.post("/translate-openai")
def rota_translate_openai(text: str):
    translated_text = translate_openai(text)
    return {"traducao": translated_text}

"""
    __________________________       __________________________
    | Usuário insere texto    | -->  | FastAPI recebe o texto |
    __________________________       __________________________

                                               |
                                               V
_____________________________       _____________________________
| OpenAI traduz para francês| <--  | LangChain prepara o prompt |
_____________________________       _____________________________

                |
                V
_____________________________       _____________________________
|   FastAPI retorna JSON     | -->  | Usuário recebe a tradução |
_____________________________       _____________________________
"""

# ------------------------------------------------------------------------------
# Questão 3
# ------------------------------------------------------------------------------