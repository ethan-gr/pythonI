## INTRODUCTION

This program is intended to convert a raw format file to a fasta format.
It's use is meant for users that have a DNA sequence embedded within a raw file, and wish to set this into a Fasta (fna) file format .

## METODOLOGY
Here is explained the most important parts of the code.
And it's cases.

#### Installation
It is only required to have Python installed

### Manage arguments

- In order for the program to work it needs the arguments in the next order:
	1. Path
	2. Sequence name
	3. Destination (Optional)

```python
args = sys.argv[1:]
```

- First the existence of the path and its status of file is confirmed
```python
rute = args[0]
if not os.path.isfile(rute):
    raise ValueError("\nDirection given doesn't exists or is not a file")
```

- Folders, name and extension extracted
```python
rute_elements = re.findall(r'[^/,\.,\\]+', rute)
```

- Check for allowed extensions (If not allowed raise error)
```python
supported_files = ['txt']
file_type = rute_elements[-1]
# Check valid file types
if file_type not in supported_files:
    raise ValueError("\nGiven file is not supported")
```

- Look for the sequence name (If not found raise error)
```python
try: sequence_name = args[1]
except: raise ValueError("\nYou have to give the sequence name as second argument")
```

- Look for the destination (If not given, saved in pwd with old file name)
```python
try: destination = args[2]
except:
    old_file_name = rute_elements[-2]
    destination = f'./{old_file_name}.fna'
```


### Convert the file

- It opens the path and get all its content in a variable
```python
dna =   open(rute).read()
```

- Then process it so it get problems fixed
```python
dna = ''.join(''.join(dna.split('\n')).split(' ')).upper()
```

- Insert spaces in the sequence
```python
dna = list(dna)
for i in range(round(len(dna)/100)):
    dna.insert((i*100)+(i-1),'\n')
dna = ''.join(dna)
```

- Check for errors or emptiness in the content (If one is detected raise error)
```python
if re.search(r'[^ATCG]', dna) or dna == '':
    raise ValueError(f'\nThe sequence has an error in it')
```

- Creates a new file with the content in the variable
```python
print(f"> {sequence_name}\n{dna}", file=open(destination, "w"))
```

- Finally it informs of the conclusion of the process by showing the name of the output file.
```python
print(f"\nThe archive was saved as: {old_file_name}.fna")
```