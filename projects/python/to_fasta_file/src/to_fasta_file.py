'''
NAME
	to_fasta_file.py
    
VERSION
    1.0
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	Convert from raw to fasta format.
    

CATEGORY
	file format
	
USAGE 

	% py to_fasta_file.py
    
    It is a program that runs in CL.
    Args:
     - Path to a file that contains the sequence
     - Sequence name
     - Expected destination and new file name (If arg not given it is saved in pwd and conserves old file name)

'''

# IMPORTS
import sys # Manage arguments
import os  # Manage arguments
import re # Manage arguments / Convert the file

#---------------------------------------------------------------

# FUNCTIONS

def isSupported(file_type):
    """
    This procedure is meant to check if the format is supported to be managed
    and stop the process if it is not.
    Args:
        file_type: It stands for the file format of the file that has been passed.
    Returns:
        None
    """
    supported_files = ['txt', 'md']
    
    if file_type not in supported_files:
        raise ValueError("\nGiven file is not supported")

#---------------------------------------------------------------

# MANAGE ARGUMENTS

args = sys.argv[1:]

# PATH
rute = args[0]
# Check existence
if not os.path.isfile(rute):
    raise ValueError("\nDirection given doesn't exists or is not a file")

# Folders, name and extention extracted
rute_elements = re.findall(r'[^/,\.,\\]+', rute)

# FILE TYPE
file_type = rute_elements[-1]
isSupported(file_type)

# SEQUENCE NAME
try: sequence_name = args[1]
except: raise ValueError("\nYou have to give the sequence name as second argument")
    
# DESTINATION
try: destination = args[2]
except:
    old_file_name = rute_elements[-2]
    destination = f'./{old_file_name}.fna'

#---------------------------------------------------------------

# CONVERT THE FILE

dna =   open(rute).read()
dna = ''.join(''.join(dna.split('\n')).split(' ')).upper()

# Comprobation of correct sequence
if re.search(r'[^ATCG]', dna) or dna == '':
    raise ValueError(f'\nThe sequence has an error in it')

dna = list(dna)
for i in range(round(len(dna)/100)):
    dna.insert((i*100)+(i-1),'\n')
dna = ''.join(dna)

# make the fastA format
print(f"> {sequence_name}\n{dna}", file=open(destination, "w"))
print(f"\nThe archive was saved as: {old_file_name}.fna")
