class Pessoa:
    def __init__(self, n: str):
        self.nome = n

    def get_nome(self) -> str:
        return self.nome

    def __str__(self):
        return self.nome
    
class Budega:
    def __init__(self, caixas: int):
        self.caixas: list[Pessoa | None] = [None]*caixas
        self.fila: list[Pessoa] = []

    def __str__(self):
        caixas = [(str(p) if p is not None else "-----") for p in self.caixas]
        caixas_str = "[" + ", ".join(caixas) + "]"
        fila = [str(p) for p in self.fila]
        fila_str = "[" + ", ".join(fila) + "]"
        return f"Caixas: {caixas_str}\nEspera: {fila_str}"
    
    def chegar(self, pessoa: Pessoa):
        self.fila.append(pessoa)

    def chamar(self, i: int):
        if i < 0 or i >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        
        if not self.fila:
            print("fail: sem clientes")
            return
        
        if self.caixas[i] is not None:
            print("fail: caixa ocupado")
            return
        self.caixas[i] = self.fila.pop(0)
        
