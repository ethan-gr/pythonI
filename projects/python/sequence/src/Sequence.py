'''
NAME
	Secuence.py
    
VERSION
    1.0
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	Tells the start codon poosition in a dna secuence and shows the transcript

CATEGORY
	
USAGE 
	% py To_fasta_file.py

'''
# Definitions
dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'

start = dna.find('TAC') # Start codon
stop = dna.find('ATT')  # Stop codon

# Prints
print(f'TAC se encuentra en la posicion {start}')
print(f'El transcrito es: {dna[start:stop]}')
