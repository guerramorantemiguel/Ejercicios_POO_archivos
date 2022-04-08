class Calificaciones:
  def __init__(self, archivo):
    self.archivo = archivo
  def leerarchivo(self):
    notas = read_csv(self.archivo)
    lista_notas = []
    asistencia = list(lista_notas["asistencia"])
    1er_parcial = list(lista_notas["1er_parcial"])
    2do_parcial = list(lista_notas["2do_parcial"])
    nombre_alumno = list(lista_notas["nombre_alumno"])
    ordinario_practicas = list(lista_notas["ordinario_practicas"])

  def aprobado(self):
    notas = read_csv(self.archivo)
    lista_notas = []
    asistencia = list(lista_notas["asistencia"])
    1er_parcial = list(lista_notas["1er_parcial"])
    2do_parcial = list(lista_notas["2do_parcial"])
    nombre_alumno = list(lista_notas["nombre_alumno"])
    ordinario_practicas = list(lista_notas["ordinario_practicas"])
    for i in range(len(self.archivo)):
      if asistencia[i]>= 0.75 and 1er_parcial[i]> 4 and 2d_prcial[i]>4 and ordinario_practicas[i]> 4 and sum(1er_parcial[i*0,3 + 2do_parcial[i]*0,3 + ordinario_practicas[i]*0,4)>5:
      printe("{}aprobado".format(nombre[i]))
      
    