class Imagen(object):
    def __init__(self, titulo, ancho, alto, filas, columnas, celdas, filtros):
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas
        self.celdas = celdas
        self.filtros = filtros

class Celda(object):
    def __init__(self, x, y, activo, color):
        self.x = x
        self.y = y
        self.activo = activo
        self.color = color