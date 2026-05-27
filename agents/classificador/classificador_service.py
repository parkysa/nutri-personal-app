from graph.state import State
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import logging

logger = logging.getLogger(__name__)

class ClassificadorService:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    def classificar_input(self, state: State):
        
        prompt = """Você é um assistente de triagem de um aplicativo de nutrição e treinos.
        Sua tarefa é ler a mensagem do usuário e descobrir o que ele quer.
        
        Classifique a intenção do usuário em estritamente UMA destas três palavras:
        - receita (se o usuário quer apenas dicas de alimentação, ingredientes ou o que cozinhar)
        - treino (se o usuário quer apenas dicas de exercícios físicos)
        - ambos (se o usuário pediu as duas coisas)
        
        Sua resposta deve conter APENAS a palavra em letras minúsculas (receita, treino ou ambos).
        Nenhuma outra palavra ou pontuação.
        """

        mensagem = state.get("mensagem")

        prompt_estruturado = ChatPromptTemplate.from_messages([
            ("system", prompt),
            ("user", "{mensagem}")
        ])

        chain = prompt_estruturado | self.llm

        resposta = chain.invoke({
            "mensagem": mensagem
        })

        classificacao = resposta.content.strip().lower()

        logger.info(f"classificacao: {classificacao}")

        return {
            "classificacao": classificacao
        }
