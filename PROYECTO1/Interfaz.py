import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog
from Analizador import analizar, tokens, errores, img
from HTML import reportes
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, Qt

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contenido = None
        self.errorDialog = ErrorDialog()
        self.mensajeExito = MensajeExito()
        uic.loadUi("GUI/interfaz.ui", self)
        self.label_2.setHidden(True)
        self.label_3.setHidden(True)
        # botones clickeados y por parámetro las funciones que desencadenan
        self.botonCargar.clicked.connect(self.browsefiles) 
        self.botonAnalizar.clicked.connect(self.analizarUI)
        self.botonReporte.clicked.connect(self.reportes)
        self.botonActualizar.clicked.connect(self.actualizar)
        self.botonOriginal.clicked.connect(self.original)
        self.botonMX.clicked.connect(self.mirrorx)
        self.botonMY.clicked.connect(self.mirrory)
        self.botonDM.clicked.connect(self.doublemirror)
        self.botonSalir.clicked.connect(exit)
    
    # función para cargar archivo
    def browsefiles(self):
        # solo acepta archivos con extensión pxla
        fname = QFileDialog.getOpenFileName(self, 'Abrir archivo', 'C:\\Users\\gerso\\Desktop\\PROGRAMACIÓN\\Python\\LENGUAJES FORMALES\\PROYECTO1', 'Text files (*.pxla)')
        if fname[0]: # si no está vacío el archivo lo lee.
            with open(fname[0], 'r') as f:
                self.contenido = f.read()
                print(self.contenido)
                self.mensajeExito.show()
    
    def analizarUI(self):
        if self.contenido == None:
            self.errorDialog.show()
        else:
            analizar(self.contenido)
            self.label_2.setHidden(False)
            self.label_3.setHidden(False)
    
    def reportes(self):
        if len(tokens) == 0:
            self.errorDialog.show()
        else:
            reportes(tokens, errores)
    
    def actualizar(self):
        # actualizando el combo box
        if len(img) != 0:
            for i in img:
                self.cBoxImg.addItem(i.titulo)

    def original(self):
        nombreImagen = self.cBoxImg.currentText()
        print(nombreImagen)
        pixmap = QPixmap("Imagenes/Original/Jpg/" + nombreImagen + ".png")
        imagen = pixmap.scaled(QSize(681,381), Qt.IgnoreAspectRatio) # Qt.KeepAspectRatio 
        self.label.setPixmap(imagen)

    def mirrorx(self):
        nombreImagen = self.cBoxImg.currentText()
        print(nombreImagen)
        pixmap = QPixmap("Imagenes/MirrorX/Jpg/" + nombreImagen + ".png")
        imagen = pixmap.scaled(QSize(681,381), Qt.IgnoreAspectRatio) # Qt.KeepAspectRatio 
        self.label.setPixmap(imagen)

    def mirrory(self):
        nombreImagen = self.cBoxImg.currentText()
        print(nombreImagen)
        pixmap = QPixmap("Imagenes/MirrorY/Jpg/" + nombreImagen + ".png")
        imagen = pixmap.scaled(QSize(681,381), Qt.IgnoreAspectRatio) # Qt.KeepAspectRatio 
        self.label.setPixmap(imagen)
    
    def doublemirror(self):
        nombreImagen = self.cBoxImg.currentText()
        print(nombreImagen)
        pixmap = QPixmap("Imagenes/DoubleMirror/Jpg/" + nombreImagen + ".png")
        imagen = pixmap.scaled(QSize(681,381), Qt.IgnoreAspectRatio) # Qt.KeepAspectRatio 
        self.label.setPixmap(imagen)
      

class ErrorDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/errorDialog.ui", self)
        # botones clickeados y por parámetro las funciones que desencadenan
        self.botonAceptar.clicked.connect(self.close)


class MensajeExito(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/mensajeExito.ui", self)
        # botones clickeados y por parámetro las funciones que desencadenan
        self.botonAceptar.clicked.connect(self.close)


# main del programa
app = QApplication(sys.argv)
gui = GUI()
gui.show()
sys.exit(app.exec_())