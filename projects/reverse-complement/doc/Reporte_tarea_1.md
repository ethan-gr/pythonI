## Metodología

- Lo primero que hice fue descargar el archivo correspondiente a la practica para posteriormente trabajar con en, así qu lo situe en la carpeta `pythonI`.
- Abrimos Git Bash y nos situamos en nuestro entorno de trabajo `pwd pythonI/`.
- Luego nos movemos a la carpeta especifica en la vamos a trabajar.
```
cd projects/reverse-complement/data/
```
- Aquí movemos el archivo desde donde se encuentra hasta donde la carpeta data.
```
mv ../../../araC_gene_sequence.txt .
```
- Aquí lo añadí a los archivos controlados por git
```
git add araC_gene_sequence.txt
```
- Se le hizo un commit al archivo.
```
git commit -m "`Ahota araC gene sequence es controlado por git`" araC_gene_sequence.txt
```
- Posteriormente se uso el comando `git status` para revisar que todo fue realizado correctamente.
- Vemos que todo salio corrctamente
***
## Comandos
```
cd projects/reverse-complement/data/

mv ../../../araC_gene_sequence.txt .

git add araC_gene_sequence.txt

git commit -m "`Ahota araC gene sequence es controlado por git`" araC_gene_sequence.txt

git status
```