from graph.state import State
from langgraph.graph import StateGraph
from agents.classificador.classificador_service import ClassificadorService

class Workflow():

    def __init__(self):
        self.workflow = StateGraph(State)
        self.classificador = ClassificadorService()
        
        
    def configura_graph(self):

        # adiciona nós
        self.workflow.add_node("classificador", self.classificador.classificar_input)
        #self.workflow.add_node("chef")
        #self.workflow.add_node("personal")

        # adiciona arestas
        self.workflow.add_edge("__start__", "classificador")
        # self.workflow.add_edge()
        # self.workflow.add_edge()
        # self.workflow.add_edge()
        # self.workflow.add_edge()

    def compila_grafo(self):
        graph = self.workflow.compile()
        return graph