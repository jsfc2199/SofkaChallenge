import random 

class Participante():
    def __init__(self,nombre,alias):
        self.nombre=nombre
        self.alias=alias
        


def preguntas(lvl):
    lvl1={"Arte y Cine":"¿Quien es Tom Holland",
          "Matematicas":"¿Cuanto es Pi?",
          "Deportes":"¿Cuanto dura un partido de fútbol?",
          "Musica":"¿Que música toca Metallica?",
          "Ciencia":"¿Cuantas patas tiene una araña?"
          }
    
    lvl2={"Arte y Cine":"¿Quien pintó la Mona Lisa",
          "Matematicas":"¿De qué fórmula es la expresión A = π*r^2?",
          "Deportes":"¿ué país fue campeón del mundial de fútbol del 2018?",
          "Musica":"¿Cual es la primera nota en la música?",
          "Ciencia":"¿Cuantos huesos tiene un cuerpo humano adulto?"
          }
    
    lvl3={"Arte y Cine":"¿Cuantos libros tiene la novela Harry Potter",
          "Matematicas":"¿Que es e=mc^2?",
          "Deportes":"¿Cuantos balones de oro tiene Mbappe?",
          "Musica":"¿Cuantas notas hay en la música?",
          "Ciencia":"¿Qué parte del cuerpo tiene 27 huesos y 35 músculos?"
          }
    
    lvl4={"Arte y Cine":"¿Quién pintó el Jardín de las Delicias",
          "Matematicas":"¿Si la velocidad es constante ¿qué pasa con la aceleración?",
          "Deportes":"¿Quién fue el primer campeón de la cahmpions league?",
          "Musica":"¿Que es # en la música?",
          "Ciencia":"¿Cuantas lunas tiene Jupiter?"
          }
    
    lvl5={"Arte y Cine":"¿De que nacionalidad era Heri Cartier Bresson",
          "Matematicas":"¿Como se llama un poliedro de 20 caras?",
          "Deportes":"¿Cuando fue el primer mundial de futbol? (año)",
          "Musica":"¿Que instrumento usa clave de sol y de fa?",
          "Ciencia":"¿Que enfermedad se caracteriza por repentinos ataques de sueño?"
          }
    
    if lvl == 1:
        lvl1.keys().ra

lvl = 1

nombre = input("Ingrese su nombre por favor: ")
alias = input("Ingrese un Alias: ")

#participante = Participante(nombre, alias)


