## INTRODUCTION
This program is intended to convert a raw format file to a fasta format.

## METODOLOGY
Here is explained the most importants parts of the code.

- First it asks the user for the rute to the original archive, and then it opens it to read its content saving it inta the variable `dna`.
```python
rute = input()
dna = open(rute).read()
```
- Then ask for information about the sequence to an apropiate otuput file.
```python
name_fasta = input()
sequence_name = input()
```
- After that it creates the file with the contentes proportionated
```python
print(f"> {sequence_name}\n{dna}", file=open(f"{name_fasta}.fna", "w"))
```
- Finally it informs of the conclution of the process by telling the nname of the output file.
