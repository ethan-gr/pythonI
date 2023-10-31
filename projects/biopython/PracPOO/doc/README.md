## INTRODUCCIÓN
El programa `PracPOO.py` contiene una clase denominada `prograMascota`, que funciona como un tipo de mascota virtual. A continuación, se presenta una descripción general de cómo funciona la clase y qué métodos y atributos están disponibles.

### Markdown Tags
#lcg #biopython

## DESCRIPCIÓN
La clase `prograMascota` se utiliza para simular el comportamiento de una mascota virtual. A continuación, se describen los atributos y métodos disponibles en esta clase.

## ATRIBUTOS
- `vivo` (bool): Indica si la mascota está viva o no.
- `hambre` (int): Representa el nivel de hambre de la mascota.
- `vida` (int): Representa el nivel de vida de la mascota. Este atributo solo existe si la mascota está viva.

## MÉTODOS
La clase `prograMascota` proporciona los siguientes métodos:
- `status`: Revisa las condiciones de hambre y puntos de vida de la mascota y modifica sus atributos en función de los mismos.
- `sacrificar`: Cambia los atributos de la mascota para que se encuentre en un estado neutral.
- `alimentar`: Alimenta a la mascota y modifica negativamente su nivel de hambre.
- `jugar`: Permite que la mascota juegue, gaste energía y aumente su nivel de hambre.
- `habla`: Hace que la mascota emita un sonido específico según el tipo de mascota.

## USO
La clase `prograMascota` se puede utilizar de la siguiente manera en un entorno de programación:
```python
# Creación de una instancia de la clase
mi_mascota = prograMascota("nombre_de_la_mascota")

# Utilización de métodos de la clase
mi_mascota.alimentar()
mi_mascota.jugar()
mi_mascota.habla()
```