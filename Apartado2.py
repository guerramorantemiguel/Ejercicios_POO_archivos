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
    practicas = list(lista_notas["practicas"])
  def notafinal():
    for i in range(len(self.archivo)):
      archivo = {"Nota 1er_parcial".format(nombre_alumno[i]): 1er_parcial[i], "Nota 2do_parcial".format(nombre_alumno[i]): 2do_parcial[i], "Nota practicas".format(nombre_alumno[i]): practicas[i]}
  sum(1er_parcial[i]*0,3 + 2do_parcial[i]*0,3 + practicas[i]*0,4)
      lista_notas.append(archivo)
    print(archivo)