class Nodo:
    def __init__(self, dato: str):
        self.dato = dato
        self.S = None
        self.A = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.Fin = self.Ini = self.actual = Nodo(homepage)
        self.C = 1
        self.Act = 1

    def visit(self, url: str) -> None:
        self.actual.S = Nodo(url)
        self.actual.S.A = self.actual
        self.actual = self.actual.S
        self.actual.S = None
        self.Fin = self.actual
        self.Act += 1
        self.C = self.Act

    def back(self, steps: int) -> str:

        if steps >= self.Act:

            self.actual = self.Ini
            self.Act = 1
            return self.actual.dato
        else:

            aux = self.actual
            for _ in range(steps):

                aux = aux.A
                self.Act -= 1
            self.actual = aux

            return self.actual.dato


    def forward(self, steps: int) -> str:
        if steps >= self.C - self.Act:
            self.Act = self.C
            self.actual = self.Fin
            return self.Fin.dato
        else:
            aux = self.actual
            for _ in range(steps):
                aux = aux.S
                self.Act +=1
            self.actual = aux
            return aux.dato

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)