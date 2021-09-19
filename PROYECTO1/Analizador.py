import re
from Reporte import Token, Error
from Clases import Imagen, Celda
from HTML import imagenHTML

# lista de tokens y errores
tokens = []
errores = []

def analizar(contenido):
    # inicializando variables
    linea = 1
    columna = 1
    buffer = ""
    centinela = "$"
    estado = 0
    i = 0
    contenido += centinela

    # autómata
    while(i < len(contenido)):
        # leyendo caracter por caracter
        c = contenido[i]

        # estado 0
        if estado == 0:
            if c == "=": # signo igual
                buffer += c
                tokens.append(Token(buffer, "Signo igual", linea, columna))
                buffer = ""
                columna += 1
            elif c == "{": # llave de apertura
                buffer += c
                tokens.append(Token(buffer, "Llave de apertura", linea, columna))
                buffer = ""
                columna += 1
            elif c == "}": # llave de cierre
                buffer += c
                tokens.append(Token(buffer, "Llave de cierre", linea, columna))
                buffer = ""
                columna += 1
            elif c == "[": # corchete de apertura
                buffer += c
                tokens.append(Token(buffer, "Corchete de apertura", linea, columna))
                buffer = ""
                columna += 1
            elif c == "]": # corchete de cierre
                buffer += c
                tokens.append(Token(buffer, "Corchete de cierre", linea, columna))
                buffer = ""
                columna += 1
            elif c == ",": # coma
                buffer += c
                tokens.append(Token(buffer, "Coma", linea, columna))
                buffer = ""
                columna += 1
            elif c == ";": # punto y coma
                buffer += c
                tokens.append(Token(buffer, "Punto y coma", linea, columna))
                buffer = ""
                columna += 1
            elif c == '"' or c == "'": # comilla simple o doble
                buffer += c 
                estado = 1
                columna += 1
            elif re.search("\d", c): # dígitos
                buffer += c 
                estado = 2
                columna += 1
            elif re.search("[A-Z]", c): # comienzo de palabra reservada
                buffer += c 
                estado = 3
                columna += 1
            elif c == "#": # comienzo de número hexadecimal
                buffer += c 
                estado = 4
                columna +=1
            elif c == "@": # comienzo de separación
                buffer += c 
                estado = 5
                columna +=1
            elif c == "\n": # salto de línea
                linea += 1
                columna = 1
            elif re.search("\s", c): # espacio en blanco
                columna += 1
            elif c == "\r": # retorno de carro
                pass
            elif c == "$": # centinela
                print("Contenido aceptado :D")
                for t in tokens:
                    print(str(t))
                print()
                for e in errores:
                    print(str(e))
            else:
                buffer += c
                columna += 1
                errores.append(Error("Caracter: '" + buffer + "' no reconocido.","Error léxico", linea, columna))  
                buffer = ""              

        # estado 1
        elif estado == 1:
            if c == '"' or c == "'": # finalización de cadena
                buffer += c 
                tokens.append(Token(buffer, "Cadena", linea, columna))
                buffer = ""
                estado = 0
                columna += 1
            elif c == "\n": # salto de línea en una cadena
                buffer += c
                linea += 1
                columna = 1
            elif c == "\r": # retorno del carro
                buffer += c
                columna += 1
            else: # cualquier letra, número o caracter especial
                buffer += c
                columna += 1

        # estado 2
        elif estado == 2:
            if re.search("\d", c): # cualquier dígito
                buffer += c
                columna += 1
            else: # si no es un dígito
                tokens.append(Token(buffer, "Entero", linea, columna))
                buffer = ""
                i -= 1
                estado = 0

        # estado 3
        elif estado == 3:
            if re.search("[A-Z]", c): # letra mayúscula
                buffer += c
                columna += 1
            else: # si no es una letra mayúscula
                if buffer == "TITULO":
                    tokens.append(Token(buffer, "Título" , linea, columna))
                elif buffer == "ANCHO":
                    tokens.append(Token(buffer, "Ancho" , linea, columna))
                elif buffer == "ALTO":
                    tokens.append(Token(buffer, "Alto" , linea, columna))
                elif buffer == "FILAS":
                    tokens.append(Token(buffer, "Filas" , linea, columna))
                elif buffer == "COLUMNAS":
                    tokens.append(Token(buffer, "Columnas" , linea, columna))
                elif buffer == "CELDAS":
                    tokens.append(Token(buffer, "Celdas" , linea, columna))
                elif buffer == "FALSE" or buffer == "TRUE":
                    tokens.append(Token(buffer, "Boolean" , linea, columna))
                elif buffer == "FILTROS":
                    tokens.append(Token(buffer, "Filtro" , linea, columna))
                elif buffer == "MIRRORX" or buffer == "MIRRORY" or buffer == "DOUBLEMIRROR":
                    tokens.append(Token(buffer, "Parámetro" , linea, columna))
                else:
                    errores.append(Error("Caracter: '" + buffer + "' no reconocido.","Error léxico", linea, columna))
                buffer = ""
                i -= 1
                estado = 0

        # estado 4
        elif estado == 4:
            # si es un número o una letra de la A a la F (número hexadecimal)
            if re.search("\d", c) or re.search("[A-F]", c): 
                buffer += c
                columna += 1
            else: # si no es un número exadecimal
                tokens.append(Token(buffer, "Número hexadecimal", linea, columna))
                buffer = ""
                i -= 1
                estado = 0

        # estado 5
        elif estado == 5:
            if c == "@": # segundo separador
                buffer += c
                estado = 6
                columna += 1
            else: 
                columna += 1
                errores.append(Error("Caracter: '" + buffer + "' no reconocido.","Error léxico", linea, columna))
                estado = 0
                buffer = ""
                i -= 1
        
        # estado 6
        elif estado == 6:
            if c == "@": # tercer separador
                buffer += c
                estado = 7
                columna += 1
            else: 
                errores.append(Error("Caracter: '" + buffer + "' no reconocido.","Error léxico", linea, columna))
                estado = 0
                buffer = ""
                i -= 1

        # estado 7
        elif estado == 7:
            if c == "@": # cuarto separador
                buffer += c
                estado = 8
                columna += 1
            else: 
                errores.append(Error("Caracter: '" + buffer + "' no reconocido.","Error léxico", linea, columna))
                estado = 0
                buffer = ""
                i -= 1

        # estado 8
        elif estado == 8:
            if c != "@": # terminación de separador
                tokens.append(Token(buffer, "Separador", linea, columna))
                buffer = ""
                i -= 1
                estado = 0
        i += 1 
    guardarDatos(tokens)

# lista de imagenes
img = []
def guardarDatos(tokens):
    titulo = ""
    ancho = ""
    alto = ""
    filas = ""
    columnas = ""
    x = ""
    y = ""
    flag = ""
    hexadecimal = ""
    celdas = []
    filtros = []
    i = 1
    for t in tokens:
        if t.tipo == "Separador" or i == len(tokens):
            # agregando la imagen a la lista de imagenes
            img.append(Imagen(titulo, ancho, alto, filas, columnas, celdas, filtros))
            titulo = ""
            ancho = ""
            alto = ""
            filas = ""
            columnas = ""
            celdas = []          
            filtros = []

        if t.tipo == "Corchete de cierre":
            celdas.append(Celda(x, y, flag, hexadecimal))
            x = ""
            y = ""
            flag = ""
            hexadecimal = ""

        # encontrando la linea de los tipos o lexemas
        linea = 0
        if t.tipo == "Título":
            linea = t.linea
        elif t.tipo == "Ancho":
            linea = t.linea
        elif t.tipo == "Alto":
            linea = t.linea
        elif t.tipo == "Filas":
            linea = t.linea
        elif t.tipo == "Columnas":
            linea = t.linea
        elif t.tipo == "Corchete de apertura":
            linea = t.linea
        elif t.tipo == "Filtro":
            linea = t.linea

        # econtrando el valor de los tipos o lexemas
        for tk in tokens:
            if tk.linea == linea and tk.tipo == "Cadena":
                titulo = tk.lexema
                titulo = titulo.replace('"', '')
                break
            elif tk.linea == linea and tk.tipo == "Entero" and ancho == "":
                ancho = int(tk.lexema)
                break
            elif tk.linea == linea and tk.tipo == "Entero" and alto == "":
                alto = int(tk.lexema)
                break
            elif tk.linea == linea and tk.tipo == "Entero" and filas == "":
                filas = int(tk.lexema)
                break
            elif tk.linea == linea and tk.tipo == "Entero" and columnas == "":
                columnas = int(tk.lexema)
                break
            elif tk.linea == linea and tk.tipo == "Entero" and x == "":
                x = int(tk.lexema)
                continue
            elif tk.linea == linea and tk.tipo == "Entero" and y == "":
                y = int(tk.lexema)
                continue
            elif tk.linea == linea and tk.tipo == "Boolean" and flag == "":
                if tk.lexema == "TRUE":
                    flag = True
                    continue
                else:
                    flag = False
                    continue
            elif tk.linea == linea and tk.tipo == "Número hexadecimal" and hexadecimal == "":
                hexadecimal = tk.lexema
                break
            elif tk.linea == linea and tk.tipo == "Parámetro":
                filtros.append(tk.lexema)
                continue
            elif linea == 0:
                break
        i +=1
    
    for i in img:
        print(i.titulo, i.ancho, i.alto, i.filas, i.columnas)
        for c in i.celdas:
            print(c.x, c.y, c.activo, c.color)
        for f in i.filtros:
            print(f)
            
    # generando las imágenes en html
    imagenHTML(img)
    