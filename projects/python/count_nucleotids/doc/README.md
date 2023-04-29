## INTRODUCTION
This program is intended to show the quantity of each nucleotids of a given sequence.

## METODOLOGY
Here is explained the most importants parts of the code.

- First it asks the user for the sequence to analyse, converting it all ti the upper mode of the letter.
```python
dna = input().upper()
```
- Then it counts all the correct letters on the sequence.
```python
As = dna.count('A')
Ts = dna.count('T')
Cs = dna.count('C')
Gs = dna.count('G')
```
- Finally it verifies if it has error on it by checking the sequence lenght and quantity of correct answers, telling if there was a mistake or printing the results depending o the sequence.
```python
if As+Ts+Gs+Cs != len(dna):
    raise ValueError(f'\nThe sequence has an error in it, it only allows A, T, C and G as input\nand the sequence contains {len(dna)-(As+Ts+Gs+Cs)} Non-valid positions\n')
else:
    print(f'The dna sequence has the following quantity of aminoacids:\n\tA: {As}\tT: {Ts}\tC: {Cs}\tG: {Gs}')
```
