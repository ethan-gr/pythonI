'''
NAME
	Piedra_Papel_Tijeras.py
    
VERSION
    1.0
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	This program is intended to be a "rock, peper, scissors" to play with.

CATEGORY
	game
	
USAGE 
	% py Piedra_Papel_Tijeras.py

'''

import random # npc choice
moves = ['piedra', 'papel', 'tijeras']

# Messages to the user
print('VAMOS A JUGAR PIEDRA PAPEL O TIJERAS!\n\
Para mas inforacion de las reglas del juego se sugiere \
leer el archivo `README.md` en la documentación del programa\n\
En este juego indicas tu movimiento con números de la siguiente manera\
\n\n\tpiedra = 0\tpapel = 1\ttijeras = 2\n')

# This is an optional loop if the user want to play again
restart = 'y'
while restart == 'y':

    # The user option made
    # in little loop with a flag to ensure the user gives a valid option
    error = True
    while error == True:
        print(f'ELIGE... ')
        choice = (int(input())) # The user choose

        if 0<=choice<=2: error = False
        else: print('no escogite un opcion valida, de nuevo...')

    npc = random.choice([0,1,2]) # npc choose randomly

    # The selections are shown
    print(f'\nElegiste {moves[choice]} y el npc eligio {moves[npc]}')

    # The game result is calculated
    if npc == choice+1 or npc == choice-2: print('Perdiste!')
    if npc == choice-1 or npc == choice+2: print('Ganaste!')
    if npc == choice: print('Empataron!')

    # The optional back to game
    print('¿Quieres volver a jugar?  y=si  n=no')
    restart = input()