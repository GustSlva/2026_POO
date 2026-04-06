class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def Calc_area(self):
        return 3.14 * self.raio ** 2
    def Calc_circu(self):
        return 2 * 3.14 * self.raio
    
x = Circulo(5)
print(x.Calc_area(), x.Calc_circu())