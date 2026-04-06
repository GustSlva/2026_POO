class Viagem:
    def __init__(self, distancia, tempo):
        self.distancia = distancia
        self.tempo = tempo
    def Velociadade_m(self):
        return self.distancia / (self.tempo/60)
    
x = Viagem(500, 200)
print(x.Velociadade_m())