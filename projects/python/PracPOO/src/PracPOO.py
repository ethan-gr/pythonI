'''
NAME
	PracPOO.py
    
VERSION
    0.0.1
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	Este programa contiene dentro de si una clase que funge como un tipo de mascota virtual

CATEGORY
	Objeto
	
USAGE

'''

# CREACIÓN DE LA CLASE
class prograMascota():
  """
  Esta clase tiene como unica función ser una mascota,
  
  Args:
    nombre, este es el nombre que se le da intrinsecamente al objeto
  """
  # Atributos
  vivo = True
  hambre = 20
  if vivo: vida = 100

  # constructor
  def __init__(self, nombre):
    self.nombre = nombre
  
  # metodos
  def status(self):
    """
    Este metodo revisa las condiciones de habre y puntos de vida del objeto
    y modifica sus atributos en función de los mismos
    """
    if self.vivo and self.hambre > 80: self.vida -= 30
    if self.vida <= 0: self.vivo = False
    
  def sacrificar(self):
    """
    Este metodo cambia los atributos del objeto para que se encuentre de manera neutral
    """
    self.vivo = False
    self.vida = 0

  def alimentar(self):
    """
    Este metodo alimenta al objeto y modifica negativamente su hambre
    """
    if self.vivo: self.hambre -= 10
    else: print(f'{self.nombre} esta muerto, no es posible alimentarlo...')
    self.status()

  def jugar(self):
    """
    Este metodo lo que hace es hacer que el objeteo juegue, gaste energía y le de hambre
    """
    if self.vivo: self.hambre += 5
    else: print(f'{self.nombre} esta muerto, no es posible jugar con el...')
    self.status()

  def habla(self):
    """
    Este metodo hace ue nuestro objeto haga un ruido
    """
    if self.vivo: print("aaahhh!")
    else: print(f'{self.nombre} esta muerto, no puede hablar...')
    self.status()

# sub-clases de prograMascota

class PERROgrama(prograMascota):
  def habla(self):
    """
    Este metodo hace ue nuestro objeto ladre
    """
    if self.vivo: print("Guau!")
    else: print(f'{self.nombre} esta muerto, no puede hablar...')

class proGrATO(prograMascota):
    """
    Este metodo hace ue nuestro objeto mauye
    """
  def habla(self):
    if self.vivo: print("Miau!")
    else: print(f'{self.nombre} esta muerto, no puede hablar...')