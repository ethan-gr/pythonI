'''
NAME
	filtro_calidad.py
    
VERSION
    0.0.1
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	El programa permite leer un archivo FASTQ y obtener el número de lecturas 
    cuyo promedio de calidad está por debajo de un umbral dado.

    ARGS
        path(str): Se refiere a la ruta en la cual se va a encontrar el archivo fastq
        threshold(int): Es aquel valor qu indica en valor de corte
        --under(bool): Indica si el corte se hará para contar las lecturas arriba de ese umbral o debajo de ese umbral
	
USAGE
    % py filtro_calidad.py [--under] <path> <threshold>

'''
#---------------------------------------------------------------
# IMPORTS
import argparse             # manage arguments
from Bio import SeqIO       # manage sequence quality

#---------------------------------------------------------------
# MANAGE ARGUMENTS
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("path", type=str, help='fastq file path')
parser.add_argument("threshold", type=int, help='threshold files value')
parser.add_argument("--under", action='store_true', help='threshold files value')
args = parser.parse_args()

#---------------------------------------------------------------
# MAIN

seqs = 0
seq_negadas = 0
for record in SeqIO.parse(args.path, "fastq"):
    seqs += 1
    if sum(record.letter_annotations["phred_quality"])/101 > args.threshold:
        seq_negadas += 1
if(args.under): print(f'sequencias por debajo del unbral: {seq_negadas}')
else: print(f'sequencias por arriba del unbral: {seqs - seq_negadas}')