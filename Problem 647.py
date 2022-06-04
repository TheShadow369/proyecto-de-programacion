"""
Problema 647
Chutes and Ladders
"""
"""
procedimiento convertInt

Entrada: cadenas de numeros enteros que representan las entradas del problema

Este procedimiento realiza la conversion de las cadenas de numeros enteros a numeros enteros.
"""

def convertInt(data):   
    for i in range(len(data)): data[i] = int(data[i])

"""
funcion chutesAndLadders

Entrada: un numero entero que representa el numero de jugadores, una lista de numeros enteros que representan los
lanzamientos de los dados, una lista de numeros enteros que representa las posiciones en la que se gana turno, una 
lista de numeros enteros que representan las posiciones en que se pierde turno, un diccionario que contienes las
posiciones de las escaleras siendo un numero entero la clave, la cual representa la posicion de inicio del tobogan o
la escalera y como valor un numero entero que representa la posicion final de la escalera o el tobogan.

Salida: un numero entero que representa quien fue el ganador del juego.
"""

def chutesAndLadders(jug, data, winT, loseT, ladder_Slide):
    win, i, j, ans = 0, 0, 0, []
    for a in range(jug): ans.append(0)

    while (i < len(data)) and (j < len(ans)) and (win == 0):
        if ans[j] >= 0:
            if ans[j] + data[i] <= 100: 
                ans[j] += data[i]

                if ans[j] in winT: i += 1

                elif ans[j] in loseT: 
                    ans[j] *= -1
                    j += 1
                    i += 1   

                elif ans[j] in ladder_Slide: 
                    ans[j] = ladder_Slide[ans[j]]
                    j += 1
                    i += 1

                else:
                    j += 1
                    i += 1  

                if ans[j-1] == 100: win = j

            else: 
                j += 1
                i += 1
        else:
            ans[j] *= -1
            j += 1

        if j > jug-1: j = 0

    return win

def leerImprimir(): 
     
    data = input().split()
    convertInt(data)

    jug = int(input())
    
    while jug != 0:
          
        ladderAndSlide = input().split()
        convertInt(ladderAndSlide)
        ladder_Slide = {}
        
        while (ladderAndSlide[0] != 0) and (ladderAndSlide[1] != 0):
            ladder_Slide[ladderAndSlide[0]] = ladderAndSlide[1]
                
            ladderAndSlide = input().split()
            convertInt(ladderAndSlide)
            
        loseWin = int(input())
        winT, loseT = [], []
        
        while (loseWin != 0):
            
            if (loseWin > 0): winT.append(loseWin)
            elif (loseWin < 0): loseT.append(abs(loseWin))
                
            loseWin = int(input())

        winer = chutesAndLadders(jug, data, winT, loseT, ladder_Slide)

        print(winer)

        jug= int(input())
    
leerImprimir()


