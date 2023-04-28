## Metodología  

- Lo primero que hice fue descargar el archivo correspondiente a la practica para posteriormente trabajar con el, así qu lo situe en la carpeta `pythonI`.
- Abrimos Git Bash y nos situamos en nuestro entorno de trabajo  es decir nuestro repositorio `pythonI/`.
- Situados en la rama `master` `pythonI` movemos los archivos a la carpeta `pythonI/projects/reverse-complement/data/`
```
mv ./projects/reverse-complement/data/araC_gene_sequence.txt .
```
- Luego nos movemos a la carpeta especifica en la vamos a trabajar `pythonI/projects/reverse-complement/data/`.
```
cd projects/reverse-complement/data/
```
- Aquí lo añadí a los archivos controlados por git
```
git add araC_gene_sequence.fna
```
- Se le hizo un commit al archivo.
```
git commit -m "Se añadio la secuencia de araC a la carpeta data" araC_gene_sequence.fna
```
- Posteriormente se uso el comando `git status` para revisar que todo fue realizado correctamente.
- Vemos que todo salio correctamente
***
## Comandos
```
mv ./projects/reverse-complement/data/araC_gene_sequence.txt .

cd projects/reverse-complement/data/

git add araC_gene_sequence.fna

git commit -m "Se añadio la secuencia de araC a la carpeta data" araC_gene_sequence.fna

git status
```