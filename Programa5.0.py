import random
import PreguntasYRespuestas
import Persona
import listaJugadores


def validarRespuesta(respuesta, score):
    if respuesta.upper() == PreguntasYRespuestas.respuestas[i].get(category):
        score = victorias[i+1]        
        print("Su respuesta es...")
        print("CORRECTA")
        print("Has ganado $" + str(score) + " dólares")
        return True
    else:
        print("Respuesta incorrecta.")
        print("Has perdido todo")
        score=0
        return False

def guardarHistoricoJugadores():
    historicoJugadores.agregarJugador(jugador.nombre)
    historicoJugadores.agregarJugador(jugador.alias)
    historicoJugadores.agregarJugador(score)
    historicoJugadores.guardarJugador()

def introduccion(lvl):    
    ganado = victorias[lvl]
    vInformativoLvlPremio=[0 for i in range (5)]
    vInformativoLvlPremio[0] = "Aquí va la pregunta #%s Por $%s dólares." % (lvl, ganado)
    vInformativoLvlPremio[1] = "Ahora vamos a la preguntan #%s para que ganes $%s dólares." % (lvl, ganado)
    vInformativoLvlPremio[2] = "Pregunta #%s por $%s dólares." % (lvl, ganado)
    vInformativoLvlPremio[3] = "Esta es la siguiente pregunta #%s que te dará $%s dólares." % (lvl, ganado)
    vInformativoLvlPremio[4] = "Ahora es el turno de la pregunta #%s. Ganarás $%s! dólares" % (lvl, ganado)
    nIntroduccionAleatoria=int(random.random()*5)
    return vInformativoLvlPremio[nIntroduccionAleatoria]

victorias=[0,500,1000,10000,45000,100000]
score = 0
lvls = [1,2,3,4,5]

nombre = input("Ingresa un nombre: ")
alias = input("Ingresa un alias de 3 letras: ")

bandera = False
while bandera==False:
    if len(alias)>3 or len(alias)<3:
        print("alias muy extenso o muy corto. Por favor intente nuevamente.")
        alias = input("Ingresa un alias de 3 letras: ")
    elif len(alias)==3:
        bandera=True

jugador = Persona.Jugador(nombre, alias)
historicoJugadores = listaJugadores.listaJugadores()


for i in range(0, len(lvls)):
    print(introduccion(i+1))
    
    category = random.choice(list((PreguntasYRespuestas.preguntas[i].keys())))
    print("La categoría es: " + category)
    print("La pregunta es: " + PreguntasYRespuestas.preguntas[i].get(category))         
    print("Opciones: " + str(PreguntasYRespuestas.opciones[i].get(category)))

    respuesta = input("Digite la opción correcta: ")

    if validarRespuesta(respuesta, score): 
        score += victorias[i+1]
        if i == 4:            
            print("Felicidades, has completado todos los niveles. Has conseguido un total de $" + str(score) + " dólares")
            guardarHistoricoJugadores()  
            break
        else:                    
            continuar = input("Desea continuar jugando (S/N): ")
        if continuar.lower()=="s":
            print("Premio acumulado: $" + str(score) + " dólares")
            print("\n")            
            continue
        else:
            print("Juego terminado")
            print("Has acumulado: $" + str(score) + " dólares")
            guardarHistoricoJugadores()               
            break
    else:
        score = 0
        guardarHistoricoJugadores()
        break
