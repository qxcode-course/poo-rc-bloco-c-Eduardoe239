class Crianca:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"{self.nome}:{self.idade}"


class PulaPula:
    def __init__(self):
        self.fila = []
        self.pula = []

    def arrive(self, nome, idade):
        self.fila.insert(0, Crianca(nome, idade))

    def enter(self):
        if len(self.fila) == 0:
            return
        crianca = self.fila.pop()
        self.pula.insert(0, crianca)

    def leave(self):
        if len(self.pula) == 0:
            return
        crianca = self.pula.pop()
        self.fila.insert(0, crianca)

    def remove(self, nome):
        for lista in [self.fila, self.pula]:
            for i, c in enumerate(lista):
                if c.nome == nome:
                    lista.pop(i)
                    return
        print(f"fail: {nome} nao esta no pula-pula")

    def show(self):
        fila_str = "[" + ", ".join(repr(c) for c in self.fila) + "]"
        pula_str = "[" + ", ".join(repr(c) for c in self.pula) + "]"
        print(f"{fila_str} => {pula_str}")


def main():
    sistema = PulaPula()
    while True:
        try:
            linha = input().strip()
        except EOFError:
            break
        if linha == "":
            continue
        partes = linha.split()
        comando = partes[0]
        print(f"${linha}")
        if comando == "arrive":
            sistema.arrive(partes[1], int(partes[2]))
        elif comando == "show":
            sistema.show()
        elif comando == "enter":
            sistema.enter()
        elif comando == "leave":
            sistema.leave()
        elif comando == "remove":
            sistema.remove(partes[1])
        elif comando == "end":
            break


main()
