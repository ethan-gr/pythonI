## INTRODUCTION
This program is intended to show the nucleotids proportions of a sequence given by an archive.

## METODOLOGY
Here is explained the most importants parts of the code.

- First it asks the user for the rute to the archive, and then it opens it to read its content saving it inta the variable `dna`.
```python
rute = input()
dna = open(rute).read()
```
- It proceds to count the 'A&T' together by adding them, same with 'C&G'.
```python
AT = dna.count('A') + dna.count('T')
CG = dna.count('C') + dna.count('G')
```
- It adds them all to get the total so it can calculate percentages.
```python
total = AT + CG
```
- Finally it informs about the results of the percentages to the user, calculing them in-print.
```python
print(f'The dna sequence has the following proportions of nucluetids:\n\
    \tAT: {AT*100/total}%\n\tCG: {CG*100/total}%')
```