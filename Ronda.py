class Ronda:
    def __init__(self,categoria,pregunta,respuesta,opciones):
        self.categoria=categoria
        self.pregunta=pregunta
        self.respuesta=respuesta
        self.opciones=opciones
    
    #Muestra la categoría, pregunta y opciones de la ronda
    def estado(self):
        print("La categoría es: " + self.categoria)
        print("La pregunta es: " + self.pregunta)         
        print("Opciones: " + self.opciones)
        
        
    