import random
import PreguntasYRespuestas
import Persona
import listaJugadores
import Ronda

def validateAnswer(answer, RightAnswer, score):
    if answer.upper() == RightAnswer:
        score = victories[i+1]        
        print("Su respuesta es...")
        print("CORRECTA")
        print("Has ganado $" + str(score) + " dólares")
        return True
    else:
        print("Respuesta incorrecta.")
        print("Has perdido todo")
        score=0
        return False

def introduccion(lvl):
    earns = victories[lvl]
    vInformativeLvlAward=[0 for i in range (5)]
    vInformativeLvlAward[0] = "Aquí va la pregunta #%s Por $%s dólares." % (lvl, earns)
    vInformativeLvlAward[1] = "Ahora vamos a la preguntan #%s para que ganes $%s dólares." % (lvl, earns)
    vInformativeLvlAward[2] = "Pregunta #%s por $%s dólares." % (lvl, earns)
    vInformativeLvlAward[3] = "Esta es la siguiente pregunta #%s que te dará $%s dólares." % (lvl, earns)
    vInformativeLvlAward[4] = "Ahora es el turno de la pregunta #%s. Ganarás $%s! dólares" % (lvl, earns)
    nRandomIntroduction=int(random.random()*5)
    return vInformativeLvlAward[nRandomIntroduction]

victories=[0,500,1000,10000,45000,100000]
score = 0
name = input("Ingresa un name: ")
alias = input("Ingresa un alias de 3 letras: ")

flag = False
while flag==False:
    if len(alias)>3 or len(alias)<3:
        print("alias muy extenso o muy corto. Por favor intente nuevamente.")
        alias = input("Ingresa un alias de 3 letras: ")
    elif len(alias)==3:
        flag=True

player = Persona.Jugador(name, alias)
playersHistory = listaJugadores.listaJugadores()

for i in range(0, 5):
    
    print(introduccion(i+1))    
    category = random.choice(list((PreguntasYRespuestas.preguntas[i].keys())))
    ronda = Ronda.Ronda(category,PreguntasYRespuestas.preguntas[i].get(category),
                        PreguntasYRespuestas.respuestas[i].get(category),
                        str(PreguntasYRespuestas.opciones[i].get(category)))
    
    ronda.estado()
    
    respuesta = input("Digite la opción correcta: ")

    if validateAnswer(respuesta, ronda.respuesta, score): 
        score += victories[i+1]
        if i == 4:            
            print("Felicidades, has completado todos los niveles. Has conseguido un total de $" + str(score) + " dólares")
            playersHistory.saveplayersHistory(player,score)  
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
            playersHistory.saveplayersHistory(player,score)               
            break
    else:
        score = 0
        playersHistory.saveplayersHistory(player,score)
        break
