#lcg #python
## Metodología

- Lo primero que hice fue descargar los archivos correspondientes: `araC_gene_sequence.fna` y `araB_gene_sequence.fna`, para posteriormente trabajar con ellos.
- Los situe en la carpeta `pythonI`.
- Abrimos Git Bash y nos situamos en nuestro entorno de trabajo  es decir nuestro repositorio `pythonI/`.
- Situados en la rama `master` `pythonI` movemos los archivos a la carpeta `pythonI/projects/reverse-complement/data/`
```
mv araB_gene_sequence.fna araC_gene_sequence.fna ./projects/reverse-complement/data/
```
- Luego nos movemos a la carpeta especifica en la vamos a trabajar `pythonI/projects/reverse-complement/data/`.
```
cd projects/reverse-complement/data/
```
- Posteriormente lo añadimos a los archivos controlados por git
```
git add araB_gene_sequence.fna
```
- Se les hicieron commits correspondientes.
```
git commit -m "Se añadio la secuencia de araB a la carpeta data" araB_gene_sequence.fna
```
- Posteriormente se uso el comando `git status` para revisar que todo fue realizado correctamente y nuestra rama detrabajo limpia.
- Posteiormente simulamos mutaciones de la secuencia en `araC_gene_sequence.fna` metiendonos dentro de este archivo con un editor en estae caso nano y cambiando tres de las letras que representan nucleotidos.
```
nano araC_gene_sequence.fna
```
- Agregamos un commit explicando las modificaciones
```
git commit -m "Se simulo la mutación del gene modificando tres caracteres" araC_gene_sequence.fna
```
- Realizamos un git status para confirmar que todo se realizó correctamente.
- Posteriormente realizamos una comparación con la version anterior del archivo.
```
git diff HEAD~1 araC_gene_sequence.fna
```
- Posteriormente realizamos una comparación con la antepenultima version del archivo.
```
git diff HEAD~2 araC_gene_sequence.fna
```
- Restauramos una versión que no tiene las mutacionnes o alteraciones.
```
git checkout HEAD~1 araC_gene_sequence.fna
```
- Se realizo un commit documentando la restauración
```
git commit -m "Se resturo la version del archivo sin las modificaciones previas" araC_gene_sequence.fna
```
- Posterior y finalmente se subieron las actualizaciones del repositorio a GitHub, en donde se incluye al reporte en la carpeta doc.
```
git push origin master
```
***
## Comandos
```
mv araB_gene_sequence.fna araC_gene_sequence.fna ./projects/reverse-complement/data/

cd projects/reverse-complement/data/

git add araB_gene_sequence.fna

git commit -m "Se añadio la secuencia de araB a la carpeta data" araB_gene_sequence.fna

git status

nano araC_gene_sequence.fna
# Aquí se hacen los respectivos cambios

git commit -m "Se simulo la mutación del gene modificando tres caracteres" araC_gene_sequence.fna

git status

git diff HEAD~1 araC_gene_sequence.fna
git diff HEAD~2 araC_gene_sequence.fna

git checkout HEAD~1 araC_gene_sequence.fna

git commit -m "Se resturo la version del archivo sin las modificaciones previas" araC_gene_sequence.fna

git push origin master
```