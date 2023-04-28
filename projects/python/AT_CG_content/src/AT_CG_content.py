'''
NAME
	AT_CG_content.py
    
VERSION
    1.0
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	It shows the nucleotids proportions of a sequence given by an archive

CATEGORY
	
USAGE 

'''


# Message to the user
print('Please, enter the archive rute wich contains the dna sequence:')
# Recive sequence
rute = input()
dna = open(rute).read()

# Count AT, CG
AT = dna.count('A') + dna.count('T')
CG = dna.count('C') + dna.count('G')
total = AT + CG

# Messages with results
print(f'The dna sequence has the following proportions of nucluetids:\n\
    \tAT: {AT*100/total}%\n\tCG: {CG*100/total}%')