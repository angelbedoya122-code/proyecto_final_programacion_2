class Polinomio:
    def __init__(self, L):
        lista_limpia = list(L)
        while len(lista_limpia) > 1 and lista_limpia[-1] == 0:
            lista_limpia.pop()
        self.L = lista_limpia
        
    def __str__(self):
        cad = f'{self.L[0]}'
        for i in range(1, len(self.L)):
            if self.L[i] >= 0:
                cad += f' + {self.L[i]}x^{i}'
            else:
                cad += f' - {abs(self.L[i])}x^{i}'
        return cad

    def __add__(self, other):
        if not isinstance(other, Polinomio):
            raise TypeError("Solo se pueden sumar objetos de la clase Polinomio")

        n1 = len(self.L)
        n2 = len(other.L)
        limite_comun = min(n1, n2)
        Lsum = [self.L[i] + other.L[i] for i in range(limite_comun)]

        if n1 > n2:
            Lsum += self.L[limite_comun:]
        else:
            Lsum += other.L[limite_comun:]

        return Polinomio(Lsum)

    def __sub__(self, other):
        if not isinstance(other, Polinomio):
            raise TypeError("Solo se pueden restar objetos de la clase Polinomio")

        polinomio_negativo = Polinomio([-i for i in other.L])
        return self + polinomio_negativo
    
    def __mul__(self, other):
        if not isinstance(other, Polinomio):
            raise TypeError("Solo se pueden multiplicar objetos de la clase Polinomio")

        longitud_final = len(self.L) + len(other.L) - 1
        Lmul = [0] * longitud_final

        for i in range(len(self.L)):
            for j in range(len(other.L)):
                Lmul[i+j] += self.L[i] * other.L[j]

        return Polinomio(Lmul)

    def evaluar(self, x):
        result = 0
        for i in range(len(self.L)):
            result += self.L[i] * (x ** i)
        return result
  

class PolinomiosDerivables(Polinomio):
    def derivada(self):
        derivada = []
        exp = 1
        for i in self.L[1:]:
            derivada.append(i * exp)
            exp += 1
        return PolinomiosDerivables(derivada if derivada else [0])

    def recta_tangente(self, x0):
        polinomio_derivado = self.derivada()
        m = polinomio_derivado.evaluar(x0)
        y0 = self.evaluar(x0)
        b = y0 - (m * x0)
        return PolinomiosDerivables([b, m])

    def grado(self):
        return f'Este polinomio es de grado {len(self.L) - 1}'