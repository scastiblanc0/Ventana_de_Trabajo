from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QWidget, QApplication, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
import os
from PIL import Image, ImageFilter

app = QApplication([])
window = QWidget()
window.setWindowTitle('')
window.resize(900, 500)


#boton de carpeta
btn_folder = QPushButton('Carpeta')

#listado 
list_filename = QListWidget()

# Linea vertical izquierda
lineVertLeft = QVBoxLayout()

lineVertLeft.addWidget(btn_folder)
lineVertLeft.addWidget(list_filename)


# Label
label_imagen = QLabel('Imagen')

# Listado de botones
bnt_left = QPushButton('Izquierda')
bnt_right = QPushButton('Derecha')
bnt_reflejo = QPushButton('Reflejo')
bnt_nitidez = QPushButton('Nitidez')
bnt_b_n = QPushButton('B/N')

# Linea Horizontal Buttons
lineBottons = QHBoxLayout()

lineBottons.addWidget(bnt_left)
lineBottons.addWidget(bnt_right)
lineBottons.addWidget(bnt_reflejo)
lineBottons.addWidget(bnt_nitidez)
lineBottons.addWidget(bnt_b_n)

# Linea Vertical Derecha
lineVertDere = QVBoxLayout()

lineVertDere.addWidget(label_imagen)
lineVertDere.addLayout(lineBottons)

# Linea Horizontal Principal
linePrincipal = QHBoxLayout()

linePrincipal.addLayout(lineVertLeft)
linePrincipal.addLayout(lineVertDere)

# Agregar a la ventana principal 
window.setLayout(linePrincipal)

# Global Variables
wordisk = ''

#class
class ImagenProccess ():
    def __init__(self, imagenes = None, nombre = None, subcarpeta = None):
        self.imagenes = imagenes
        self.nombre = nombre
        self.subcarpeta = subcarpeta

    def upLoadFile(self, filename):
        self.filename = filename
        # Unir la ruta de la carpeta con el nombre del archivo
        path_file = os.path.join(wordisk, filename)
        self.image = Image.open(path_file)# abrir imagen

    def showFile(self, path_file):
        label_imagen.hide()
        pixmapImagen = QPixmap(path_file)
        width, height = 900, 500
        pixmapImagen = pixmapImagen.scaled(width, height, Qt.KeepAspectRatio)
        label_imagen.setPixmap(pixmapImagen)
        label_imagen.show()

    def saveFile(self):
        new_path = os.path.join(wordisk, self.subcarpeta)
        if not os.path.exists(new_path) or not os.path.isdir(new_path):
            os.mkdir(new_path)
        new_path_file = os.path.join(new_path, self.filename)
        self.image.save(new_path_file)

    def blackAndWhite(self):
        self.image = self.image.convert('L')
        self.saveFile()
        new_path = os.path.join(wordisk, self.subcarpeta, self.filename)
        self.showFile(new_path)
    
    def sharpness(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveFile()
        new_path = os.path.join(wordisk, self.subcarpeta, self.filename)
        self.showFile(new_path)
    


imagenEditor = ImagenProccess(subcarpeta='efects')

# Funciones
def showFolder():
    global wordisk
    wordisk = QFileDialog.getExistingDirectory()
    filenames = os.listdir(wordisk)
    extenciones = ['jpg', 'png', 'jpeg', 'bmp']


    result = filterFiles(filenames, extenciones)
    list_filename.addItems(result)

def filterFiles(filenames, extenciones):
    result = []
    for file in filenames:
        for extencion in extenciones:
            if file.endswith(extencion):
                result.append(file)

    return result

def choiceFileImagen():
    if list_filename.currentRow() >= 0:
        filename = list_filename.currentItem().text()
        imagenEditor.upLoadFile(filename)
        path_file = os.path.join(wordisk, filename)
        imagenEditor.showFile(path_file)



btn_folder.clicked.connect(showFolder)
list_filename.itemClicked.connect(choiceFileImagen)
bnt_b_n.clicked.connect(imagenEditor.blackAndWhite)
bnt_nitidez.clicked.connect(imagenEditor.sharpness)

#Ejecutar la aplicacion
window.show()
app.exec_()
