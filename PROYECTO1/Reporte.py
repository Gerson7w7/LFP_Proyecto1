class Token(object):
    def __init__(self, lexema, tipo, linea, columna):
        self.lexema = lexema
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def __str__(self):
        cadena = self.lexema + "; " + self.tipo + "; " + str(self.linea) + "; " + str(self.columna)
        return cadena
        

class Error(object):
    def __init__(self, descrip, tipo, linea, columna):
        self.descrip = descrip
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
    
    def __str__(self):
        cadena = self.descrip + "; " + self.tipo + "; " + str(self.linea) + "; " + str(self.columna)
        return cadena