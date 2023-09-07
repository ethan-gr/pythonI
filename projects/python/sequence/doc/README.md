## INTRODUCTION
This program is intended to tell the user the the start codon poosition in a dna secuence and show the transcript produced by start and stop codons.

It only analise an in-code sequence but that is something easily fixable and ask the user for it.

### Markdown Tags
#lcg #python

## METODOLOGY
Here is explained the most importants parts of the code.

- The content of the variable `dna` is declared.
```python
dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'
```
- Then we look for the correspondent codons, these are introduced in-code also.
```python
start = dna.find('TAC')
stop = dna.find('ATT')
```
- Finally the information about the transcript is displayed
```python
print(f'TAC se encuentra en la posicion {start}')
print(f'El transcrito es: {dna[start:stop]}')
```