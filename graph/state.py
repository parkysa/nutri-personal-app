from typing import Optional, TypedDict

class State(TypedDict):
    mensagem: str
    ingredientes: list[str]
    objetivo: str
    receita: Optional[str]
    treino: Optional[str]
    classificacao: str
    
