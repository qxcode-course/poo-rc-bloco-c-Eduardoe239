class Grafite:
    def __init__(self, c: float, d: str, t: int):
        self.calibre = c
        self.dureza = d
        self.tamanho = t

    def desgaste(self):
        tb = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}
        return tb.get(self.dureza, 1)
    
    def __str__(self):
        return f"{self.calibre}:{self.dureza}:{self.tamanho}"
    
class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico = None
        self.tambor = []

    def inserir(self, grafite: Grafite):
        if grafite.calibre != self.calibre:
            print("fail: calibre incompatível")
            return
        self.tambor.append(grafite)

    def puxar(self):
        if self.bico is not None:
            print("fail: já existe grafite no bico")
            return
        if len(self.tambor) == 0:
            print("fail: tambor vazio")
            return
        self.bico = self.tambor.pop(0)

    def remover(self):
        if self.bico is None:
            print("fail: não existe grafite no bico")
            return
        self.bico = None

    def escrever(self):
        if self.bico is None:
            print("fail: não existe grafite no bico")
            return
        
        gasto = self.bico.gasto_por_folha()

        if self.bico.tamanho <=10:
            print("fail: tamanho insuficiente")
            return
        if self.bico.tamanho - gasto < 10:
            print("fail: folha incompleta")
            self.bico.tamanho = 10
            return
        self.bico.tamanho -= gasto

    def mostrar(self):
        bico_str = "[]" if self.bico is None else f"[{self.bico}]"
        tambor_str = "".join(f"[{g}]" for g in self.tambor)
        print(f"calibre: {self.calibre}, bico: {bico_str}")

    