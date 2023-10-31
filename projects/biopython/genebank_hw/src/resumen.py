'''
NAME
	resumen.py
    
VERSION
    0.0.1
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	Regresa la información del gb dado y la información de las secuencias deseadas

    ARGS
        path(str): Se refiere a la ruta en la cual se va a encontrar el archivo genebank
        G(str): Es una lista de genes de los cuales quiero las secuencias
	
USAGE
    % py resumen.py <path> G <genes>

'''
#---------------------------------------------------------------
# IMPORTS

import argparse             # manage arguments
from Bio import SeqIO       # manage sequence quality

#---------------------------------------------------------------
# MANAGE ARGUMENTS

parser = argparse.ArgumentParser(description='Regresa la información del gb dado y la información de las secuencias deseadas.')
parser.add_argument("path", type=str, help='genebank file path')
parser.add_argument('genes', metavar='N', type=str, nargs='+', help='Genes to return')
args = parser.parse_args()

#---------------------------------------------------------------
# MAIN

for gb_record in SeqIO.parse(args.path, "genbank"):
    print(f"Organismo: {gb_record.annotations['organism']}")
    print(f"fecha:{gb_record.annotations['date']}")
    print(f"País: {gb_record.features[0].qualifiers['country'][0]}")
    print(f"Aislado: {gb_record.features[0].qualifiers['isolation_source'][0]}")

    for gen in args.genes:
        for feature in gb_record.features:
            if 'gene' and 'translation' in feature.qualifiers.keys() and feature.qualifiers['gene'][0] == gen:
                seq = gb_record.seq[feature.location.nofuzzy_start:feature.location.nofuzzy_end]
                print(f"Gen: {feature.qualifiers['gene'][0]}")
                print(f"ADN: {seq}")
                print(f"ARN: {seq.transcribe()}")
                print(f"Proteína: {feature.qualifiers['translation'][0]}") # | print(seq.translate())
