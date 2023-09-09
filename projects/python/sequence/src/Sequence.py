'''
NAME
	Secuence.py
    
VERSION
    1.1
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	Tells the start codon posicion in a dna secuence and shows the transcript
	in a sequence given by the user

CATEGORY
	
USAGE 
	% py Sequence.py <START CODON> <STOP CODON>

'''
# IMPORTS
import sys # Manage arguments
import os # Manage arguments
import re  # Detection of sequence cases

#---------------------------------------------------------------
# MANAGE ARGUMENTS

args = sys.argv[1:]

# PATH
path = args[0]
# Check existence
if not os.path.isfile(path):
    raise ValueError("\nDirection given doesn't exists or is not a file")

dna =   open(path).read()
# we identify if is fastA to make proper changes
dna = dna.split('\n')
if re.search(r'.fna$', path):
    dna = dna[1:]
dna = ''.join(''.join(dna).split(' ')).upper()

# Comprobation of correct sequence
if re.search(r'[^ATCG]', dna) or dna == '':
    raise ValueError(f'\nThe sequence has an error in it')


# CODONS
startCodon = args[1].upper()
stopCodon = args[2].upper()

#---------------------------------------------------------------
# FUNCTIONS

def transcrit(sequence, startCodon, stopCodon, retrn='transcrit'):
	'''
	This function works with a sequence looking for the transcript by 
	checking for the star and stop codon, it can return the transcrit 
	or the start of the transcrit

	Args:
		- sequence: Is the string that contains the sequence
		- startCodon: It defines the codon identified as start
		- stoptCodon: It defines the codon identified as stop
		- retrn: It can be two options ´tarnscrit´ or ´start´ and it
				 defines what to return
	Retuns:
		- ´sequence[start:stop]´: The transcrit
		- start: The position in which the transcript start
	'''
	# The search
	start = sequence.find(startCodon)
	stop = sequence.find(stopCodon)
	if start == None or stop == None:
		raise ValueError('It is not posible to find the tarnscript due to codons ausense')

	# Returns
	if retrn == 'transcrit': return sequence[start:stop]
	elif retrn == 'start': return start
	else: raise ValueError('The parameter retrn has is not in an acceptable parameter')


#---------------------------------------------------------------
# MAIN

print(f"{startCodon} se encuentra en la posicion {transcrit(dna, startCodon, stopCodon, 'start')}\n\
      El transcrito es: {transcrit(dna, startCodon, stopCodon)}")

print('el programa ha terterminado')