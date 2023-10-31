## INTRODUCCIÓN

El programa `resumen.py` está diseñado para extraer información de un archivo GeneBank y proporcionar información detallada sobre los genes especificados. A continuación, se presenta una descripción general de cómo funciona el programa y cómo se pueden utilizar los argumentos.

### Markdown Tags
#lcg #biopython

## CÓMO FUNCIONA
El programa analiza el archivo GenBank especificado y extrae información relevante, como el organismo, la fecha, el país y el aislamiento. Luego, busca los genes especificados y proporciona detalles adicionales, como la secuencia de ADN, ARN y la proteína correspondiente.

## ARGUMENTOS
El programa acepta los siguientes argumentos:
- `path` (str): La ruta al archivo GenBank que se va a analizar.
- `genes` (List[str]): Una lista de genes de los cuales se desean obtener las secuencias y la información asociada.

## USO
Para ejecutar el programa, utiliza el siguiente comando:
```shell
% python resumen.py <path> G <genes>
```
### EJEMPLO DE USO
1. Para obtener información detallada de los genes 'gen1' y 'gen2' del archivo GeneBank:
```shell
python resumen.py example.gb G gen1 gen2
```