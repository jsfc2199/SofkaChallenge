from io import open
class listaJugadores:
    jugadores = []
 
    def agregarJugador(self,j):        
        self.jugadores.append(j)
        
    def guardarJugador(self):
        listaDeJugadores = open("HistoricoJugadores.txt","a")
        listaDeJugadores.write(str(self.jugadores))
        listaDeJugadores.write("\n")
        listaDeJugadores.close()
        
    def saveplayersHistory(self,player,score):
        self.agregarJugador(player.nombre)
        self.agregarJugador(player.alias)
        self.agregarJugador(score)
        self.guardarJugador()