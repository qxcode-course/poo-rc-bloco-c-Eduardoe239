class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def desgaste(self):
        tabela = {
            "HB": 1,
            "2B": 2,
            "4B": 4,
            "6B": 6
        }
        return tabela.get(self.dureza, 1)

    def __str__(self):
        return f"{self.calibre}:{self.dureza}:{self.tamanho}"


class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico = None
        self.tambor = []

    def insert(self, grafite: Grafite):
        if grafite.calibre != self.calibre:
            print("fail: calibre incompatível")
            return
        self.tambor.append(grafite)

    def pull(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return
        if len(self.tambor) == 0:
            print("fail: tambor vazio")
            return
        self.bico = self.tambor.pop(0)

    def remove(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        self.bico = None

    def write(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return

        gasto = self.bico.desgaste()

        if self.bico.tamanho <= 10:
            print("fail: tamanho insuficiente")
            return

        if self.bico.tamanho - gasto < 10:
            print("fail: folha incompleta")
            self.bico.tamanho = 10
            return

        self.bico.tamanho -= gasto

    def show(self):
        bico_str = "[]" if self.bico is None else f"[{self.bico}]"
        tambor_str = "".join(f"[{g}]" for g in self.tambor)
        print(f"calibre: {self.calibre}, bico: {bico_str}, tambor: <{tambor_str}>")


def main():
    lap = None

    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if line == "":
            continue

        print(f"${line}")
        cmd = line.split()
        op = cmd[0]
        if op == "end":
            break

        if op == "init":
            lap = Lapiseira(float(cmd[1]))

        elif op == "insert":
            cal = float(cmd[1])
            dur = cmd[2]
            tam = int(cmd[3])
            lap.insert(Grafite(cal, dur, tam))
        
        elif op == "pull":
            lap.pull()

        elif op == "remove":
            lap.remove()

        elif op == "write":
            lap.write()

        elif op == "show":
            lap.show()

        else:
            print("fail: comando invalido")


main()