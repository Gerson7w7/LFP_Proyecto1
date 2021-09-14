import webbrowser as wb
import imgkit

def reportes(tokens, errores):
        repTokens(tokens)
        repErrores(errores)
        wb.open_new(r'C:\\Users\\gerso\Desktop\\PROGRAMACIÓN\\Python\\LENGUAJES FORMALES\\PROYECTO1\\Reportes\\Tokens.html')
        wb.open_new(r'C:\\Users\\gerso\Desktop\\PROGRAMACIÓN\\Python\\LENGUAJES FORMALES\\PROYECTO1\\Reportes\\Errores.html')

def repTokens(tokens):
        i = 1
        html = open("Reportes/Tokens.html", 'w')
        html.write('<!DOCTYPE html><!--Declarar el tipo de cumento -->'
                + '<html>'
                + '<!--Encabezado-->'
                + '<head>'
                + '<meta charset="UTF-8"><!--codififcaion de caracteres ñ y á-->'
                + '<meta name="name" content="Reporte"><!--nombre de la pagina-->'
                + '<meta name="description" content="name"><!--autor de la pagina-->'
                + '<meta name="keywods" content="uno,dos,tres"><!--Palabras claavez para, separadas por comas-->'
                + '<meta name="robots" content="Index, Follow"><!--Mejora la busqueda-->'
                + '<meta name="viewport" content="width=device-width, initial-scale=1"><!--visibilidaad en diferentes pantallas -->'
                + '<link rel="stylesheet" type="text/css" href="css/styles.css"/><!--css /estilo/tipo/ruta relativa -->'
                + '<title>Tokens</title><!--Titulo visible de la pagina-->'
                + '</head>'
                + '<body>'
                + '<center><!--centra todos lo que este dentro-->'
                + '<h6 class="titulos"><b> TOKENS </b></h6>')
        html.write('<br>  <br>  <br>'
                + '<!----tabla 2-->'
                + '<table class="steelBlueCols">'
                + '<thead>'
                + '<tr> <th>No.</th> <th>Token</th> <th>Lexema</th> <th>Fila</th> <th>Columna</th> </tr>'
                + '</thead>'
                + '<tbody>')
        for t in tokens:
                html.write(f'<tr> <td>{str(i)}</td> <td>{t.tipo}</td> <td>{t.lexema}</td> <td>{str(t.linea)}</td> <td>{str(t.columna)}</td></tr>') 
                i += 1
        html.write('</tbody>'
                + '</table>'
                + '<!----termina tabla 2-->'
                + '<br>  <br>  <br>'
                + '</center>'
                + '</body>'
                + '</html>')
        html.close()


def repErrores(errores):
        i = 1
        html = open("Reportes/Errores.html", 'w')
        html.write('<!DOCTYPE html><!--Declarar el tipo de cumento -->'
                + '<html>'
                + '<!--Encabezado-->'
                + '<head>'
                + '<meta charset="UTF-8"><!--codififcaion de caracteres ñ y á-->'
                + '<meta name="name" content="Reporte"><!--nombre de la pagina-->'
                + '<meta name="description" content="name"><!--autor de la pagina-->'
                + '<meta name="keywods" content="uno,dos,tres"><!--Palabras claavez para, separadas por comas-->'
                + '<meta name="robots" content="Index, Follow"><!--Mejora la busqueda-->'
                + '<meta name="viewport" content="width=device-width, initial-scale=1"><!--visibilidaad en diferentes pantallas -->'
                + '<link rel="stylesheet" type="text/css" href="css/styles.css"/><!--css /estilo/tipo/ruta relativa -->'
                + '<title>Errores</title><!--Titulo visible de la pagina-->'
                + '</head>'
                + '<body>'
                + '<center><!--centra todos lo que este dentro-->'
                + '<h6 class="titulos"><b> ERRORES </b></h6>')
        html.write('<br>  <br>  <br>'
                + '<!----tabla 2-->'
                + '<table class="steelBlueCols">'
                + '<thead>'
                + '<tr> <th>No.</th> <th>Fila</th> <th>Columna</th> <th>Caracter</th></tr>'
                + '</thead>'
                + '<tbody>')
        for e in errores:
                html.write(f'<tr> <td>{str(i)}</td> <td>{str(e.linea)}</td> <td>{str(e.columna)}</td> <td>{e.descrip}</td></tr>') 
                i += 1
        html.write('</tbody>'
                + '</table>'
                + '<!----termina tabla 2-->'
                + '<br>  <br>  <br>'
                + '</center>'
                + '</body>'
                + '</html>')
        html.close()


def imagenHTML(img):
        original(img)
        mirrorx(img)
        mirrory(img)
        doublemirror(img)


def original(img):
        for i in img:
                html = open(f"Imagenes/Original/{i.titulo}.html", 'w')
                html.write('<!DOCTYPE html><!--Declarar el tipo de cumento -->'
                        + '<html>'
                        + '<!--Encabezado-->'
                        + '<head>'
                        + '<meta charset="UTF-8"><!--codififcaion de caracteres ñ y á-->'
                        + '<meta name="name" content="Reporte"><!--nombre de la pagina-->'
                        + '<meta name="description" content="name"><!--autor de la pagina-->'
                        + '<meta name="keywods" content="uno,dos,tres"><!--Palabras claavez para, separadas por comas-->'
                        + '<meta name="robots" content="Index, Follow"><!--Mejora la busqueda-->'
                        + '<meta name="viewport" content="width=device-width, initial-scale=1"><!--visibilidaad en diferentes pantallas -->'
                        + f'<title>{i.titulo}</title><!--Titulo visible de la pagina-->'
                        + '</head>'
                        + '<body>'
                        + '<center><!--centra todos lo que este dentro-->'
                        + f'<h1 class="titulos"><b> {i.titulo} </b></h1>')
                html.write('<br>  <br>'
                        + '<table border cellspacing=0 class="default">')

                f = 0
                for filas in range(i.filas):
                        c = 0
                        html.write('<tr>')
                        for columnas in range(i.columnas):
                                flag = True
                                for celda in i.celdas:
                                        # si está en la lista de celdas se pintará, de lo contrario no
                                        # width = ancho, height = alto
                                        if c == celda.x and f == celda.y and celda.activo == True:
                                                html.write(f'<td style="width:{i.ancho/i.columnas}px; height:{i.alto/i.filas}px;" bgcolor="{celda.color}"></td>')
                                                flag = False
                                                break
                                if flag == True:
                                        html.write(f'<td style="width:{i.ancho/i.columnas}px; height:{i.alto/i.filas}px;"></td>')
                                c += 1
                        html.write('</tr>')
                        f += 1

                html.write('</tbody>'
                        + '</table>'
                        + '<!----termina tabla 2-->'
                        + '<br>  <br>'
                        + '</center>'
                        + '</body>'
                        + '</html>')
                html.close()

        # pasando las imagenes html a png
        for i in img:
                imgkit.from_file(f'Imagenes/Original/{i.titulo}.html', f'Imagenes/Original/Jpg/{i.titulo}.png')


def mirrorx(img):
        for i in img:
                html = open(f"Imagenes/MirrorX/{i.titulo}.html", 'w')
                html.write('<!DOCTYPE html><!--Declarar el tipo de cumento -->'
                        + '<html>'
                        + '<!--Encabezado-->'
                        + '<head>'
                        + '<meta charset="UTF-8"><!--codififcaion de caracteres ñ y á-->'
                        + '<meta name="name" content="Reporte"><!--nombre de la pagina-->'
                        + '<meta name="description" content="name"><!--autor de la pagina-->'
                        + '<meta name="keywods" content="uno,dos,tres"><!--Palabras claavez para, separadas por comas-->'
                        + '<meta name="robots" content="Index, Follow"><!--Mejora la busqueda-->'
                        + '<meta name="viewport" content="width=device-width, initial-scale=1"><!--visibilidaad en diferentes pantallas -->'
                        + f'<title>{i.titulo}</title><!--Titulo visible de la pagina-->'
                        + '</head>'
                        + '<body>'
                        + '<center><!--centra todos lo que este dentro-->'
                        + f'<h1 class="titulos"><b> {i.titulo} </b></h1>')
                html.write('<br>  <br>'
                        + '<table border cellspacing=0 class="default">')

                f = 0
                for filas in range(i.filas):
                        c = i.columnas - 1
                        html.write('<tr>')
                        for columnas in range(i.columnas, 0, -1):
                                flag = True
                                for celda in i.celdas:
                                        # si está en la lista de celdas se pintará, de lo contrario no
                                        # width = ancho, height = alto
                                        if c == celda.x and f == celda.y and celda.activo == True:
                                                html.write(f'<td style="width:{i.ancho/i.columnas}px; height:{i.alto/i.filas}px;" bgcolor="{celda.color}"></td>')
                                                flag = False
                                                break
                                if flag == True:
                                        html.write(f'<td style="width:{i.ancho/i.columnas}px; height:{i.alto/i.filas}px;"></td>')
                                c -= 1
                        html.write('</tr>')
                        f += 1

                html.write('</tbody>'
                        + '</table>'
                        + '<!----termina tabla 2-->'
                        + '<br>  <br>'
                        + '</center>'
                        + '</body>'
                        + '</html>')
                html.close()

        # pasando las imagenes html a png
        for i in img:
                imgkit.from_file(f'Imagenes/MirrorX/{i.titulo}.html', f'Imagenes/MirrorX/Jpg/{i.titulo}.png')


def mirrory(img):
        for i in img:
                html = open(f"Imagenes/MirrorY/{i.titulo}.html", 'w')
                html.write('<!DOCTYPE html><!--Declarar el tipo de cumento -->'
                        + '<html>'
                        + '<!--Encabezado-->'
                        + '<head>'
                        + '<meta charset="UTF-8"><!--codififcaion de caracteres ñ y á-->'
                        + '<meta name="name" content="Reporte"><!--nombre de la pagina-->'
                        + '<meta name="description" content="name"><!--autor de la pagina-->'
                        + '<meta name="keywods" content="uno,dos,tres"><!--Palabras claavez para, separadas por comas-->'
                        + '<meta name="robots" content="Index, Follow"><!--Mejora la busqueda-->'
                        + '<meta name="viewport" content="width=device-width, initial-scale=1"><!--visibilidaad en diferentes pantallas -->'
                        + f'<title>{i.titulo}</title><!--Titulo visible de la pagina-->'
                        + '</head>'
                        + '<body>'
                        + '<center><!--centra todos lo que este dentro-->'
                        + f'<h1 class="titulos"><b> {i.titulo} </b></h1>')
                html.write('<br>  <br>'
                        + '<table border cellspacing=0 class="default">')

                f = i.filas - 1
                for filas in range(i.filas, 0, -1):
                        c = 0
                        html.write('<tr>')
                        for columnas in range(i.columnas):
                                flag = True
                                for celda in i.celdas:
                                        # si está en la lista de celdas se pintará, de lo contrario no
                                        # width = ancho, height = alto
                                        if c == celda.x and f == celda.y and celda.activo == True:
                                                html.write(f'<td style="width:{i.ancho/i.columnas}px; height:{i.alto/i.filas}px;" bgcolor="{celda.color}"></td>')
                                                flag = False
                                                break
                                if flag == True:
                                        html.write(f'<td style="width:{i.ancho/i.columnas}px; height:{i.alto/i.filas}px;"></td>')
                                c += 1
                        html.write('</tr>')
                        f -= 1

                html.write('</tbody>'
                        + '</table>'
                        + '<!----termina tabla 2-->'
                        + '<br>  <br>'
                        + '</center>'
                        + '</body>'
                        + '</html>')
                html.close()

        # pasando las imagenes html a png
        for i in img:
                imgkit.from_file(f'Imagenes/MirrorY/{i.titulo}.html', f'Imagenes/MirrorY/Jpg/{i.titulo}.png')


def doublemirror(img):
        for i in img:
                html = open(f"Imagenes/DoubleMirror/{i.titulo}.html", 'w')
                html.write('<!DOCTYPE html><!--Declarar el tipo de cumento -->'
                        + '<html>'
                        + '<!--Encabezado-->'
                        + '<head>'
                        + '<meta charset="UTF-8"><!--codififcaion de caracteres ñ y á-->'
                        + '<meta name="name" content="Reporte"><!--nombre de la pagina-->'
                        + '<meta name="description" content="name"><!--autor de la pagina-->'
                        + '<meta name="keywods" content="uno,dos,tres"><!--Palabras claavez para, separadas por comas-->'
                        + '<meta name="robots" content="Index, Follow"><!--Mejora la busqueda-->'
                        + '<meta name="viewport" content="width=device-width, initial-scale=1"><!--visibilidaad en diferentes pantallas -->'
                        + f'<title>{i.titulo}</title><!--Titulo visible de la pagina-->'
                        + '</head>'
                        + '<body>'
                        + '<center><!--centra todos lo que este dentro-->'
                        + f'<h1 class="titulos"><b> {i.titulo} </b></h1>')
                html.write('<br>  <br>'
                        + '<table border cellspacing=0 class="default">')

                f = i.filas - 1
                for filas in range(i.filas, 0, -1):
                        c = i.columnas - 1
                        html.write('<tr>')
                        for columnas in range(i.columnas, 0, -1):
                                flag = True
                                for celda in i.celdas:
                                        # si está en la lista de celdas se pintará, de lo contrario no
                                        # width = ancho, height = alto
                                        if c == celda.x and f == celda.y and celda.activo == True:
                                                html.write(f'<td style="width:{i.ancho/i.columnas}px; height:{i.alto/i.filas}px;" bgcolor="{celda.color}"></td>')
                                                flag = False
                                                break
                                if flag == True:
                                        html.write(f'<td style="width:{i.ancho/i.columnas}px; height:{i.alto/i.filas}px;"></td>')
                                c -= 1
                        html.write('</tr>')
                        f -= 1

                html.write('</tbody>'
                        + '</table>'
                        + '<!----termina tabla 2-->'
                        + '<br>  <br>'
                        + '</center>'
                        + '</body>'
                        + '</html>')
                html.close()

        # pasando las imagenes html a png
        for i in img:
                imgkit.from_file(f'Imagenes/DoubleMirror/{i.titulo}.html', f'Imagenes/DoubleMirror/Jpg/{i.titulo}.png')