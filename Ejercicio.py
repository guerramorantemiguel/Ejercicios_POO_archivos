class Calificaciones:
  def __init__(self, archivo):
    self.archivo = archivo
  def leerarchivo(self):
    notas = read_csv(self.archivo)
    