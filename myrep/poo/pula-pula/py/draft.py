class Crianca:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"{self.nome}:{self.idade}"
    
    class PulaPula:
        def __init__(self):
            self.fila_espera = []
            self.no_pula_pula = []

        def chegar(self, nome: str, idade: int):
            self.fila_espera.append(Crianca(nome, idade))

        def entrar(self):
            if not self.fila_espera:
                return
            crianca = self.fila_espera.pop(0)
            self.no_pula_pula.append(crianca)

        def sair(self):
            if not self.no_pula_pula:
                return
            crianca = self.no_pula_pula.pop(0)
            self.fila_espera.append(crianca)
        
        def remover(self, nome: str):
            for c in self.fila_espera:
                if c.nome == nome:
                    self.fila_espera.remove(c)
                    return

        def mostrar(self):
            fila = ", ".join(map(str, self.fila_espera))
            dentro = ", ".join(map(str, self.no_pula_pula))
            print(f"[{fila}] => [{dentro}]")
