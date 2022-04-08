class Calificaciones:
  def __init__(self, archivo):
    self.archivo = archivo
  def leerarchivo(self):
    notas = read_csv(self.archivo)
    lista_notas = []
    asistencia = list(notas["asistencia"])
    1er_parcial = list(notas["1er_parcial"])
    2do_parcial = list(notas["2do_parcial"])
    nombre_alumno = list(notas["nombre_alumno"])
    
    
    