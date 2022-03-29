#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 19:20:08 2022

@author: jose
"""
import sys
import os
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QPlainTextEdit, QPushButton, QMessageBox, QListWidget 
from PyQt5.QtGui import QIcon
from pathlib import Path

path = None

class OpcionesVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):        
        self.setWindowTitle('Editor de texto') #Colocamos un nombre a la ventana creada
        self.setGeometry(300,300,800,400) #Establecemos las dimensiones a la ventana
        self.setWindowIcon(QIcon('logo.png'))

        boton_carpeta = QPushButton('Carpeta', self)
        boton_carpeta.resize(boton_carpeta.sizeHint())
        boton_carpeta.clicked.connect(self.buscarArchivos)
        boton_carpeta.move(700, 20)

        boton_abrir = QPushButton('Abrir', self)
        boton_abrir.resize(boton_abrir.sizeHint())
        boton_abrir.clicked.connect(self.abrir_archivo)
        boton_abrir.move(700, 100)
        
        boton_guardar2 = QPushButton('Guardar', self)
        boton_guardar2.resize(boton_guardar2.sizeHint())
        boton_guardar2.clicked.connect(self.guardar_normal)
        boton_guardar2.move(700, 150)
        
        boton_guardar = QPushButton('Guardar como', self)
        boton_guardar.resize(boton_guardar.sizeHint())
        boton_guardar.clicked.connect(self.guardar_archivo)
        boton_guardar.move(685, 200)
        
        boton_cerrar = QPushButton('Cerrar', self)
        boton_cerrar.clicked.connect(self.cerrar_archivo)
        boton_cerrar.resize(boton_cerrar.sizeHint())
        boton_cerrar.move(700, 250)
        
        boton_salir = QPushButton('Salir', self)
        boton_salir.clicked.connect(QApplication.instance().quit)
        boton_salir.resize(boton_salir.sizeHint())
        boton_salir.move(700, 300)
        
        self.contenido = QPlainTextEdit(self);
        self.contenido.setGeometry(300, 50, 373, 300)
        
        self.contenido2 = QPlainTextEdit(self);
        self.contenido2.setGeometry(25, 20, 650, 25)
        self.contenido2.setReadOnly(True)
        
        self.contenido3 = QListWidget(self);
        self.contenido3.setGeometry(25, 50, 230, 300)
        
    def abrir_archivo(self):
        home_dir = str(Path.home())
        archivo, ok = QFileDialog.getOpenFileName(self,'Abrir archivo', home_dir)
        global path
        path = archivo

        if ok:
            with open(archivo, 'r') as f:
                self.path = archivo
                self.contenido.insertPlainText(''.join(f.readlines()))    
        
    def guardar_archivo(self):
        home_dir = str(Path.home())
        archivo, ok = QFileDialog.getSaveFileName(self, 'Guardar archivo', home_dir)

        if ok:
            with open(archivo, 'w') as f:
                f.write(self.contenido.toPlainText())

    def cerrar_archivo(self):
        self.contenido.clear()
        self.contenido2.clear()
        self.contenido3.clear()
        
    def guardar_normal(self):
        with open(path, 'w') as f:
            f.write(self.contenido.toPlainText())
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Advertencia',"¿Seguro que desea salir?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            
        else:
            event.ignore()  
 
    def buscarArchivos(self):
        home_dir = str(Path.home())
        archivo = QFileDialog.getExistingDirectory(self, 'Seleccionar carpeta', home_dir)
        
        self.contenido2.appendPlainText(archivo)
        
        ejemplo_dir = archivo
        contenido5 = os.listdir(ejemplo_dir)
        
        for fichero in contenido5:
            if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.txt'):
                self.contenido3.addItem(fichero) 
                
                

def main():
    app = QApplication(sys.argv)
    ov = OpcionesVentana()
    ov.show()
    

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()