# Integração de modelos de linguagem com FastAPI e LangChain

Este projeto demonstra como disponibilizar modelos de linguagem por meio de uma API construída com FastAPI. Os exercícios abrangem geração de texto com GPT-2, tradução com modelos Helsinki-NLP, integração com a API da OpenAI usando GPT-4.1-mini e testes com um Fake LLM, que simula respostas predefinidas.

## Instalação das dependências

Com o ambiente virtual ativado, execute o comando abaixo na pasta que contém o arquivo `requirements.txt`.

```bash
python -m pip install -r requirements.txt
```

## Estrutura do projeto

| Arquivo | Função |
| --- | --- |
| `main.py` | Ponto de entrada da aplicação. Inicializa o FastAPI e registra as rotas da API. |
| `models.py` | Configura GPT-2, Helsinki-NLP, GPT-4.1-mini e o Fake LLM. Reúne as funções chamadas pelas rotas. |
| `routers.py` | Define as rotas da API. Cada rota recebe a requisição, chama a função correspondente em `models.py` e devolve o resultado. |
| `requirements.txt` | Lista as dependências Python necessárias para executar o projeto. |
| `dissertacao.pdf` | Reúne as respostas dissertativas e os diagramas de fluxo solicitados nos exercícios. |
