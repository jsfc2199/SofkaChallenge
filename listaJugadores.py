from io import open
class listaJugadores:
    jugadores = []

    #agrega al jugador en la lista jugadores
    def agregarJugador(self,j):        
        self.jugadores.append(j)
    
    #creará un archivo txt y escribe los datos del jugador en el mismo
    def guardarJugador(self):
        listaDeJugadores = open("HistoricoJugadores.txt","a")
        listaDeJugadores.write(str(self.jugadores))
        listaDeJugadores.write("\n")
        listaDeJugadores.close()
    
    #llama a las funciones anteriores, guardando el nombre, alias y el puntaje ganado por el jugador en el archivo txt
    def guardarHistoricoJugador(self,jugador,puntaje):
        self.agregarJugador(jugador.nombre)
        self.agregarJugador(jugador.alias)
        self.agregarJugador(puntaje)
        self.guardarJugador()