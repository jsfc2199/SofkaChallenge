import random
from io import open
import PreguntasYRespuestas

class Jugador:
    def __init__(self,nombre,alias):
        self.nombre=nombre
        self.alias=alias
        print("Esta jugando el participante {}. AKA: {}".format(self.nombre, self.alias))
        print("\n")
        
class listaJugadores:
    jugadores = []
 
    def agregarJugador(self,j):        
        self.jugadores.append(j)
        
    def guardarJugador(self):
        listaDeJugadores = open("HistoricoJugadores.txt","a")
        listaDeJugadores.write(str(self.jugadores))
        listaDeJugadores.write("\n")
        listaDeJugadores.close()

score = 0
lvls = [1,2,3,4,5]
victorias=[0,500,1000,10000,45000,100000]

nombre = input("Ingresa un nombre: ")
alias = input("Ingresa un alias de 3 letras: ")

bandera = False
while bandera==False:
    if len(alias)>3 or len(alias)<3:
        print("alias muy extenso o muy corto. Por favor intente nuevamente.")
        alias = input("Ingresa un alias de 3 letras: ")
    elif len(alias)==3:
        bandera=True

jugador = Jugador(nombre, alias)
miLista = listaJugadores()

def introduccion(lvl):    
    ganado = victorias[lvl]
    v=[0 for i in range (5)]
    v[0] = "Aquí va la pregunta #%s Por $%s dólares." % (lvl, ganado)
    v[1] = "Ahora vamos a la preguntan #%s para que ganes $%s dólares." % (lvl, ganado)
    v[2] = "Pregunta #%s por $%s dólares." % (lvl, ganado)
    v[3] = "Esta es la siguiente pregunta #%s que te dará $%s dólares." % (lvl, ganado)
    v[4] = "Ahora es el turno de la pregunta #%s. Ganarás $%s! dólares" % (lvl, ganado)
    n=int(random.random()*5)
    return v[n]
        
for i in range(0, len(lvls)):
    print(introduccion(i+1))
    category = random.choice(list((PreguntasYRespuestas.preguntas[i].keys())))
    print("La categoría es: " + category)
    print("La pregunta es: " + PreguntasYRespuestas.preguntas[i].get(category))         
    print("Opciones: " + str(PreguntasYRespuestas.opciones[i].get(category)))

    respuesta = input("Digite la opción correcta: ")

    if respuesta.upper() == PreguntasYRespuestas.respuestas[i].get(category):
        score += victorias[i+1]
        print("Su respuesta es...")
        print("CORRECTA")
        
        print("Has acumulado $" + str(score) + " dólares")
        
        if i == 4:
            print("Felicidades, has completado todos los niveles. Has conseguido un total de $" + str(score) + " dólares")
            miLista.agregarJugador(jugador.alias)
            miLista.agregarJugador(score)  
            miLista.guardarJugador()   
            break
        else:                    
            continuar = input("Desea continuar jugando (S/N): ")
        if continuar.lower()=="s":
            print("\n")
            continue
        else:
            print("Juego terminado")
            print("Has ganado: $" + str(score) + " dólares")
            miLista.agregarJugador(jugador.alias)
            miLista.agregarJugador(score) 
            miLista.guardarJugador()                
            break
    else:
        print("Respuesta incorrecta.")
        print("Has perdido todo")
        score = 0
        miLista.agregarJugador(jugador.alias)
        miLista.agregarJugador(score) 
        miLista.guardarJugador()  
        break
