class Pessoa:
    def __init__(self, n: str):
        self.nome = n

    def __str__(self):
        return self.nome


class Budega:
    def __init__(self, caixas: int):
        self.caixas = [None] * caixas
        self.fila = []

    def __str__(self):
        caixas = [(str(p) if p is not None else "-----") for p in self.caixas]
        fila = [str(p) for p in self.fila]
        return f"Caixas: [{', '.join(caixas)}]\nEspera: [{', '.join(fila)}]"

    def chegar(self, pessoa: Pessoa):
        self.fila.append(pessoa)

    def chamar(self, i: int):
        if i < 0 or i >= len(self.caixas):
            print("fail: caixa inexistente")
            return

        if self.caixas[i] is not None:
            print("fail: caixa ocupado")
            return

        if len(self.fila) == 0:
            print("fail: sem clientes")
            return

        self.caixas[i] = self.fila.pop(0)

    def finalizar(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return

        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return

        self.caixas[index] = None


def main():
    budega = None

    while True:
        try:
            line = input().strip()
        except:
            break

        if not line:
            continue

        print(f"${line}")  # <-- ESSENCIAL para passar nos testes

        parts = line.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "end":
            break

        elif cmd == "init":
            budega = Budega(int(args[0]))

        elif cmd == "show":
            print(budega)

        elif cmd == "arrive":
            budega.chegar(Pessoa(args[0]))

        elif cmd == "call":
            budega.chamar(int(args[0]))

        elif cmd == "finish":
            budega.finalizar(int(args[0]))


main()
