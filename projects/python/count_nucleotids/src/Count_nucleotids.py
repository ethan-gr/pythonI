'''
NAME
	Count_nucleotids.py
    
VERSION
    1.0
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	It shows the quantity of each nucleotids of a given sequence

CATEGORY
	
USAGE 

'''
# Message to the user
print('Please, enter the dna sequence:')
# Recive sequence
dna = input().upper()

# Count A, T, C, G
As = dna.count('A')
Ts = dna.count('T')
Cs = dna.count('C')
Gs = dna.count('G')

# Messages with results
if As+Ts+Gs+Cs != len(dna):
<<<<<<< HEAD
<<<<<<< Updated upstream
    print('The sequence has an error in it, it only allows A, T, C and G as input')
else:
    print(f'The dna sequence has the following quantity of aminoacids:\n\
            \tA: {As}\tT: {Ts}\tC: {Cs}\tG: {Gs}')
=======
    raise ValueError('The sequence has an error in it, it only allows A, T, C and G as input')
else:
    print(f'The dna sequence has the following quantity of aminoacids:\n\
            \tA: {As}\tT: {Ts}\tC: {Cs}\tG: {Gs}')

#if dna.count("N") > 0:
#        raise ValueError(f'Sequence contains {dna.count("N")} N\'s')
>>>>>>> Stashed changes
=======
    print('The sequence has an error in it, it only allows A, T, C and G as input')
else:
    print(f'The dna sequence has the following quantity of aminoacids:\n\
            \tA: {As}\tT: {Ts}\tC: {Cs}\tG: {Gs}')
>>>>>>> b9d98c9252a20a02d1afa9e32ea48d3d69510b42
