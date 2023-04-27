'''
NAME
	To_fasta_file.py
    
VERSION
    1.0
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION

	Convert from raw to fasta format.
	
	It ask for a dna sequence in a txt file, ask for some data about and generate a fasta file whith the sequence

CATEGORY

	dna sequence
	
USAGE 

	% py To_fasta_file.py

'''

# Message to the user
print('Please, enter the archive rute wich contains the dna sequence:')
# Receive sequence
rute = input()
dna = open(rute).read()

# Ask for the new file name
print('Please, enter the expected output file name:')
name_fasta = input()

# Ask for the sequence name
print('Please, enter the sequence name:')
sequence_name = input()

# make the fastA format
print(f"> {sequence_name}\n{dna}", file=open(f"{name_fasta}.fna", "w"))
print(f"\nThe archive was saved as: {name_fasta}.fna")


