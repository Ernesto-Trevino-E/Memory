# Nombre: Ernesto Trevino
# Matricula: A00827928
# Memorama : Animales

import random
#funcion que nos ayuda a verificar si el tiro es uno posible
def leer_tiro(tablero,t,juego):
    tiro=int(input('Escoga posicion: '))
    #primer filtro para checar que este en el rango de opciones
    while (tiro == t or tiro > 35 or tiro < 0):
        tiro = int(input('Opcion no disponible, escoga otra: '))
    ren= tiro//6
    col= tiro%6
    tiro= tablero[ren][col]
    #segundo filtro que checa si la opcion ya es una carta
    #desplegada
    while (str(tiro) in juego[ren][col]):
        tiro = int(input('Opcion no disponible, escoga otra: '))
        ren= tiro//6
        col= tiro%6
        tiro= tablero[ren][col]
    #ultimo filtro para checar si el tiro no es igual a ti tiro
    #anterior, si pasa los firltros, el tiro se vuelve lo que esta
    #en esa posicion en el tablero con numeros de
    # 0 a 35 y regresa el tiro
    if (tiro != t):
        ren= tiro//6
        col= tiro%6
        tiro= tablero[ren][col]
        t = tiro
    return t
#regresa el tiro para su uso proximo
        
        #funcion que nos dira si conseguimos pares
def tablero_jugador(tablero,juego,t1,t2):
    ren1 = t1//6
    col1 = t1%6
    ren2 = t2//6
    col2 = t2%6
    #convierte ambos tiros a lo que seria en el juego de pares
    tablero[ren1][col1]=juego[ren1][col1]
    tablero[ren2][col2]=juego[ren2][col2]
    desplegar(tablero)
    #despliega las opciones escogidas
    #los ifs checan si son pares
    if (juego[ren1][col1]==juego[ren2][col2]):
        t1='si'
        t2='si'
        print('Son pares')
        following=input('<Enter para continuar>')
        #si son par, imprimer que son par y los tiros los cambia
        #a un valor string para regresarlos y agregar puntos
    elif (juego[ren1][col1]!=juego[ren2][col2]):
        tablero[ren1][col1]=t1
        tablero[ren2][col2]=t2
        print('No son pares')
        following=input('<Enter para continuar>')
        
    return tablero,t1,t2

#se utliza para mostrar el prgreso del juego, en otras funciones
#se hacen los "updates" por si sacan par
def desplegar(matriz):
    for renglon in matriz:
        for elemento in renglon:
            print(f'{elemento:>10}', end = '  ')
        #saltar de renglon
        print()

#crea los dos tableros del juego sin valores asignados 
def crear_tableros(tam_ren, tam_col):
    matriz = []
    for ren in range(tam_ren):
        matriz.append([0] * tam_col)
    return matriz
    
#introduce los numeros al tablero que vera el jugador y regresa para uso
def inicializar_tablero(matriz):
    adding=0
    for iR in range(len(matriz)):
        for iC in range(len(matriz[iR])):
            matriz[iR][iC]=adding
            adding=adding+1
    
    return(matriz)

#introduce los pares dependiendo del tema y la regresa para su uso
def inicializar_juego(matriz):
    matriz[0]=['oso','flamingo','perro','leon','tigre','perico']
    matriz[1]=['humano','elefante','leopardo','aguila','delfin','piglet']
    matriz[2]=['ganso','gato','cocodrilo','canguro','lagarto','raton']
    matriz[3]=['oso','flamingo','perro','leon','tigre','perico']
    matriz[4]=['humano','elefante','leopardo','aguila','delfin','piglet']
    matriz[5]=['ganso','gato','cocodrilo','canguro','lagarto','raton']
    
    
    return(matriz)
#las opciones que tiene el jugador,la tabla se inizia mostrando
#el tema del juego, al igual que sus posiciones
#lo deje asi para que pudiera probarlo y ya despues elegir el jugarlo al azar
def menu():
    return int(input('''1. iniciar juego memorama
2. "Randomize" tablero del juego
0. Salir
Teclea la opcion: '''))

def main():
    #en el main, primero se crean los tableros y despues
    #llenamos los tableros, uno con lo que ve el jugador
    #y el segundo el que tiene las respuestas
    tablero = crear_tableros(6,6) # vista al usuario
    juego = crear_tableros(6,6)   # detras del juego
    
    print('TABLERO')
    #Se llena de numeros del 0-35 por ser una tabla de 6x6
    inicializar_tablero(tablero)
    #muestra la tabla
    desplegar(tablero)
    print('')
    print('JUEGO')
    #tabla con 17 pares que da a los 36 lugares de la tabla anterior
    inicializar_juego(juego)
    #muestra la tabla
    desplegar(juego)
    #desplega las opciones
    opcion = menu()
    
    while opcion != 0:
        #La opcion uno es lo que correponde el juego
        if (opcion == 1):
            pointsP1=0
            pointsP2=0
            res='si'
            #el juego conitnua mientras la res sea si y los puntos
            #acumulados sea menor de 19, para que sea posible el empate
            #donde ambos consiguieron 18, y 18x18=36
            while (pointsP1+pointsP2 < 19 and res == 'si'):
                desplegar(tablero)
                print('Jugador #1 empieze-')
                t1j1= leer_tiro(tablero,-1,juego)
                t2j1= leer_tiro(tablero,t1j1,juego)
                tablero,t1j1,t2j1= tablero_jugador(tablero,juego,t1j1,t2j1)
                if (t1j1 == 'si' and t2j1 == 'si'):
                    pointsP1 = pointsP1+1
                    #por esto si es par se regresa con valore
                    #string 'si' para agregar un punto a ese jugador
       
                res= input('Desea continuar? <si><no>: ')
                #si consigue o no, pregunta si desea continuar
                #para que el segundo jugador comienze
                if (res == 'si'):
                    desplegar(tablero)
                    print('Jugador #2 empieze-')
                    t1j2= leer_tiro(tablero,-1,juego)
                    t2j2= leer_tiro(tablero,t1j2,juego)
                    tablero,t1j2,t2j2= tablero_jugador(tablero,juego,t1j2,t2j2)
                    if (t1j2 == 'si' and t2j2 == 'si'):
                        pointsP2 = pointsP2 + 1
                        #como explique antes, se agrega punto si es par
                        #y regresa el tiro con el valor string 'si'
                        
                    res = input('Desea continuar? <si><no>:')
                    #preguntar si desea seguir para que el
                    #primer jugador juegue de nuevo
             #en el caso que se dea terminar el juego o
            #la suma es mas o igual a 18(empate)
            if (res != 'si' or pointsP1+pointsP2 >= 18):
                print('-Juego Terminado-')
                #muestra la puntuacion de cada jugador
                input('Presione <ENTER> para mostrar puntiacion')
                print('Puntuacion de jugador #1: ', pointsP1)
                print('Puntuacion de jugador #2: ', pointsP2)
        #poner posiblidades donde gana 1 o 2 o empate.
                if (pointsP1 > pointsP2):
                    print ('Jugador #1 gano')
                    input('Enter para continuar')
                    
                elif (pointsP2 > pointsP1):
                    print ('Jugador #2 gano')
                    input('Enter para continuar')
                    
                elif (pointsP1 == pointsP2):
                    print ('EMPATE')
                    input('Enter para continuar')
                main()
        #Al elegir 2 la tabla consigue las posiciones al azar para
        #un juego mas entretenido
        elif (opcion == 2):
            for iR in range(len(juego)):
                random.shuffle(juego[iR])
            random.shuffle(juego)
        
        opcion=menu()
#Se llama a la funcion principal para iniciar el proceso para iniciar el juego
main()