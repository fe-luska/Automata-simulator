# Fernando Lucas Vieira Souza - 12703069

class Automato:
    def __init__(self, n_estados: int, terminais: list, n_estados_iniciais: list[int], estados_aceitacao: list[int]):
        self.n_estados = n_estados
        self.terminais = terminais
        self.n_estados_iniciais = n_estados_iniciais
        self.estados_aceitacao = estados_aceitacao
        self.transicoes = {}

    def add_transicao(self, estado_origem: int, terminal: str, estado_destino: int):
        if estado_origem not in self.transicoes:
            self.transicoes[estado_origem] = {}
        
        if terminal not in self.transicoes[estado_origem]:
            self.transicoes[estado_origem][terminal] = []
        
        self.transicoes[estado_origem][terminal].append(estado_destino)
        return
    
    def processar(self, cadeia: str):

        for estado_inicial in self.n_estados_iniciais:
            if self.processar_recursivo(estado_inicial, cadeia):
                return True
        
        return False
    
    def processar_recursivo(self, estado: int, cadeia: str) -> bool:
        if len(cadeia) == 0:
            return estado in self.estados_aceitacao

        if estado not in self.transicoes:
            return False

        if cadeia[0] not in self.transicoes[estado]:
            return False
        
        for estado_destino in self.transicoes[estado][cadeia[0]]:
            if self.processar_recursivo(estado_destino, cadeia[1:]):
                return True
        

n_estados: int = int(input("")) # 1 <= n <= 10
terminais: list[str] = input("").split()[1:]
estados_iniciais: list[int] = list(map(int, input("").split())) # AFD = 1; AFN = 1 <= n <= 10

if estados_iniciais == [1]: # nesse caso, é um AFD cujo o estado inicial é o 0
    estados_iniciais = [0]

estados_aceitacao: list[int] = list(map(int, input("").split()[1:]))
n_transicoes: int = int(input("")) # 1 <= n <= 50

automato = Automato(n_estados, terminais, estados_iniciais, estados_aceitacao)

for i in range(n_transicoes):
    transicao = input("").split() # ex: 3 a 1 (estado 3 leva ao estado 1 com o terminal 'a')
    automato.add_transicao(int(transicao[0]), transicao[1], int(transicao[2]))

n_cadeias: int = int(input("")) # 1 <= n <= 10

for i in range(n_cadeias):
    cadeia = input() # '-' para cadeia vazia
    if automato.processar(cadeia):
        print("aceita")
    else:
        print("rejeita")