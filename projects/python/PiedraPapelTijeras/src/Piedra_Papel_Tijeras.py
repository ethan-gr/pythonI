#PIEDRA_PAPEL_TIJERAS
import random
moves = ['piedra', 'papel', 'tijeras']

print('VAMOS A JUGAR PIEDRA PAPEL O TIJERAS!\n\
En este juego indicas tu movimiento con números de la siguiente manera\
\n\n\tpiedra = 0\tpapel = 1\ttijeras = 2\
\n\nELIGE... ')

choice = (int(input()))
npc = random.choice([0,1,2])
print(f'Elegiste {moves[choice]} y el npc eligio {moves[npc]}')

if npc == choice+1 or npc == choice-2: print('Perdiste!')
if npc == choice-1 or npc == choice+2: print('Ganaste!')
if npc == choice: print('Empataron!')