from dotenv import load_dotenv
from graph.state import State
from graph.workflow import Workflow

class NutriPersonalApp():

    def __init__(self):
        load_dotenv()
        self.workflow = Workflow()
        self.workflow.configura_graph()  
        self.compiled_graph = self.workflow.compila_grafo() 

    def _boas_vindas(self):
        print("=" * 50)
        print("BEM-VINDO AO ASSISTENTE DE DIETA E TREINO SMART")
        print("=" * 50)
        print("\nPor favor, informe seu objetivo (receita, treino ou ambos) e os ingredientes disponíveis.")
        print("Exemplo: 'Quero o combo hoje. Tenho frango, ovo e batata doce. Foco em ganho de massa.'")
        return input("\nDigite aqui: ")
    
    def _resultado(self, resultado):
        print("\n" + "=" * 50)
        print("RESULTADO DO SEU ASSISTENTE SMART")
        print("=" * 50)
        print(resultado)

    def _run(self):

        entrada = self._boas_vindas()

        estado_inicial: State = {
            "mensagem": entrada,   
            "ingredientes": [],             
            "objetivo": "",
            "receita": None,
            "treino": None,
            "classificacao": None
        }

        resultado = self.compiled_graph.invoke(estado_inicial)

        return resultado

if __name__ == "__main__":
    app = NutriPersonalApp()
    app._resultado(app._run())

