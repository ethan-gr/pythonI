## INTRODUCCIÓN

Este programa, llamado `filtro_calidad.py` tiene como objetivo analizar un archivo FASTQ y determinar el número de lecturas cuyo promedio de calidad está por debajo o por encima de un umbral específico, según la preferencia del usuario. A continuación, se proporciona una descripción general de cómo funciona el programa.

### Markdown Tags
#lcg #biopython

## CÓMO FUNCIONA
El programa recorre el archivo FASTQ especificado y evalúa la calidad de las lecturas en función del umbral proporcionado. Luego, muestra el número de lecturas que cumplen con los criterios especificados.

## ARGUMENTOS
El programa acepta los siguientes argumentos:
- `path` (str): La ruta al archivo FASTQ que se va a analizar.
- `threshold` (int): El valor umbral que se utilizará para realizar el análisis.
- `--under` (opcional): Indica si se desea contar las lecturas por debajo del umbral (utilizando esta bandera) o por encima del umbral (sin la bandera).

## USO
Para ejecutar el programa, utiliza el siguiente comando:
```shell
% python filtro_calidad.py [--under] <path> <threshold>
```
### EJEMPLOS DE USO
1. Para contar las secuencias de calidad por debajo del umbral (umbral: 30):
```shell
python filtro_calidad.py --under ejemplo.fastq 30
```
2. Para contar las secuencias de calidad por encima del umbral (umbral: 25):
```shell
python filtro_calidad.py ejemplo.fastq 25
```