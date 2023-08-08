'''
NAME
	Secuence.py
    
VERSION
    1.1
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	Tells the start codon poosition in a dna secuence and shows the transcript
	in a sequence given by the user

CATEGORY
	
USAGE 
	% py To_fasta_file.py

'''

def transcrit(sequence, startCodon='TAC', stopCodon='ATT', retrn='transcrit'):
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


# Prints
print('Ingresa una secuencia a la cual buscar el punto d inicio del transcrito tanto como el transcrito')
dna = input().upper()

print(f"TAC se encuentra en la posicion {transcrit(dna, retrn='start')}\n\
      El transcrito es: {transcrit(dna)}")

print('el programa ha terterminado')
