#### ¿Cómo es que funciona Git?
Crea un repositorio que es la carpeta que lleva el seguimiento de los csambios que se registran en el codigo.
Es una mala idea tener repositorios anidados dentro de

### Comandos:
`git add`:
	Pone comp una especie de bandera, que indica que empieze a controlar dicho archivo. y genera una carpeta oculta `.git` la cual solo sirve para el funcionamiento del repositorio.
	
`git comit`:
	Es como tomarle a una foto en la cual basicamente esto es el registro de los archivos.
	`git commit -m`:
		Este nos permite añadir un leyenda a un documento indicando el cambio. La buene¿a practica es añadir un mensaje y el nombre del archivo al que va a controlar.
	`git commit -a:
		Este lo que hace es añadir un 'archivo' en el cual mas bien es como una especie de documentacion al respecto de los cambio que le hacemos.
	`git commit --amend -m "Mensaje"`:
		Este nos permite modificar uel comentario del ultimo commit que hicimos.
	
`git diff`:
	`git diff --stage:
		Este nos permite revisar los cambios que se presentan de un archivo a comparacion de su ultimo commit.
	
`git status`:
	Lo que hace es indicarnos el estado de los elementos en la carpeta que estamos, nos atuda a visualizar com estamos haciendo los comandos y como van  los archivos
	`git status -u`:
		Este le dice a git que busque los archivos dentro del init inclusive  si no le hemos indicado a git que lo controle.
	
`git log`:
	Es una lista de los commits que se llevaron a cabo.
	`git log -n`:
		donde n es un numero, esto muestroa los ultimos n comentarios
 `checkout`:
	 Es la manera de regresar a una de las versiones anteriores, se le da el identificador que condeguimos con `log --oneline` y el nombre del archivo

#### Ramas en Git
No son algo que veremos pero es una caracterristica importante de Github porque lo que permite es para ir modificando los camnbios de manera acoplada.