'''
NAME
	AT_CG_content.py
    
VERSION
    1.0
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	It shows the nucleotids proportions of a given sequence

CATEGORY
	
USAGE
    % py AT_CG_content.py <path>

'''

# IMPORTS
import sys # Manage arguments
import os # Manage arguments
import re  # Detection of sequence cases

#---------------------------------------------------------------
# MANAGE ARGUMENTS

args = sys.argv[1:]

# PATH
rute = args[0]
# Check existence
if not os.path.isfile(rute):
    raise ValueError("\nDirection given doesn't exists or is not a file")

#---------------------------------------------------------------
# MAIN

dna =   open(rute).read()
# we identify if is fastA to make proper changes
dna = dna.split('\n')
if re.search(r'.fna$', rute):
    dna = dna[1:]
dna = ''.join(''.join(dna).split(' ')).upper()

# Comprobation of correct sequence
if re.search(r'[^ATCG]', dna) or dna == '':
    raise ValueError(f'\nThe sequence has an error in it')

# Count AT, CG
AT = dna.count('A') + dna.count('T')
CG = dna.count('C') + dna.count('G')
total = AT + CG

# Messages with results
print(f'The dna sequence has the following proportions of nucluetids:\n\
    \tAT: {AT*100/total}%\n\tCG: {CG*100/total}%')