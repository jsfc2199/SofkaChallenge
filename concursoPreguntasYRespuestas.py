import random
import PreguntasYRespuestas
import Persona
import listaJugadores
import Ronda

#valida si la respuesta ingresada por el usuario es correcta y dirá cuánto ganó en la ronda o si respondió mal y perdió todo
def validarRespuesta(respuesta, respuestaCorrecta, puntaje):
    if respuesta.upper() == respuestaCorrecta:
        puntaje = victorias[i+1]        
        print("Su respuesta es...")
        print("CORRECTA")
        print("Has ganado $" + str(puntaje) + " dólares")
        return True
    else:
        print("Respuesta incorrecta.")
        print("Has perdido todo")
        puntaje=0
        return False

#realiza una introducción aleatoria a la pregunta de la ronda correspondiente
def introduccion(nivel):
    ganado = victorias[nivel]
    introduccionPregunta=[0 for i in range (5)]
    introduccionPregunta[0] = "Aquí va la pregunta #%s Por $%s dólares." % (nivel, ganado)
    introduccionPregunta[1] = "Ahora vamos a la preguntan #%s para que ganes $%s dólares." % (nivel, ganado)
    introduccionPregunta[2] = "Pregunta #%s por $%s dólares." % (nivel, ganado)
    introduccionPregunta[3] = "Esta es la siguiente pregunta #%s que te dará $%s dólares." % (nivel, ganado)
    introduccionPregunta[4] = "Ahora es el turno de la pregunta #%s. Ganarás $%s! dólares" % (nivel, ganado)
    introduccionRandom=int(random.random()*5)
    return introduccionPregunta[introduccionRandom]

#muestra el final del juego en caso de que el jugador no quiera responder al pregunta y lo guarda en el historico de jugadores
def finDelJuego():
    print("Juego terminado")
    print("Has acumulado: $" + str(puntaje) + " dólares")
    historicoJugagores.guardarHistoricoJugador(jugador,puntaje)  

victorias=[0,500,1000,10000,45000,100000]
puntaje = 0
nombre = input("Ingresa un nombre: ")
alias = input("Ingresa un alias de 3 letras: ")

#verifica la longitud del alias
bandera = False
while bandera==False:
    if len(alias)>3 or len(alias)<3:
        print("alias muy extenso o muy corto. Por favor intente nuevamente.")
        alias = input("Ingresa un alias de 3 letras: ")
    elif len(alias)==3:
        bandera=True

jugador = Persona.Jugador(nombre, alias)
historicoJugagores = listaJugadores.listaJugadores()

#ejecuta el ciclo del juego hasta que el jugador pierda, complete todas las rondas o quiera salirse del juego
for i in range(0, 5):
    
    print(introduccion(i+1))    
    categoria = random.choice(list((PreguntasYRespuestas.preguntas[i].keys())))
    ronda = Ronda.Ronda(categoria,PreguntasYRespuestas.preguntas[i].get(categoria),
                        PreguntasYRespuestas.respuestas[i].get(categoria),
                        str(PreguntasYRespuestas.opciones[i].get(categoria)))
    
    ronda.estado()
    
    responderPregunta = input("Desea responder la pregunta(S/N): ")
        
    if responderPregunta.lower()=="s":  
        respuesta = input("Digite la opción correcta: ")
        if validarRespuesta(respuesta, ronda.respuesta, puntaje): 
            puntaje += victorias[i+1]
            if i == 4:            
                print("Felicidades, has completado todos los niveles. Has conseguido un total de $" + str(puntaje) + " dólares")
                historicoJugagores.guardarHistoricoJugador(jugador,puntaje)  
                break
            else:                    
                print("Premio acumulado: $" + str(puntaje) + " dólares")
                print("\n")            
                continue            
        else:
            puntaje = 0
            historicoJugagores.guardarHistoricoJugador(jugador,puntaje)
            break
    else:  
        finDelJuego()
        break


    
