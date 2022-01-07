class Jugador:
    def __init__(self,nombre,alias):
        self.nombre=nombre
        self.alias=alias
        print("Esta jugando el participante {}. AKA: {}".format(self.nombre, self.alias))
        print("\n")
