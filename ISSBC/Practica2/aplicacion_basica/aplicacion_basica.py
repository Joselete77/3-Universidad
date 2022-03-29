#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:07:25 2022

@author: jose
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

app = QtWidgets.QApplication(sys.argv)

class calculadora(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        
        self.variable1 = QtWidgets.QLineEdit("")
        self.variable2 = QtWidgets.QLineEdit("")
        self.sumar = QtWidgets.QPushButton("+")
        self.restar = QtWidgets.QPushButton("-")
        self.multiplicar = QtWidgets.QPushButton("*")
        self.dividir = QtWidgets.QPushButton("/")
        self.resultado = QtWidgets.QLineEdit("")
        
        centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(centralwidget)
        grid = QtWidgets.QGridLayout(centralwidget)
        
        grid.addWidget(self.variable1,0,1,1,3)
        grid.addWidget(self.variable2,1,1,1,3)
        grid.addWidget(self.sumar,2,0)
        grid.addWidget(self.restar,2,1)
        grid.addWidget(self.multiplicar,2,2)
        grid.addWidget(self.dividir,2,3)
        grid.addWidget(self.resultado,3,1,1,3)
        
        grid.addWidget(QtWidgets.QLabel("Variable A"),0,0)
        grid.addWidget(QtWidgets.QLabel("Variable B"),1,0)  
        grid.addWidget(QtWidgets.QLabel("Resultado"),3,0)                      
        
        self.sumar.clicked.connect(self.suma)
        self.restar.clicked.connect(self.resta)
        self.multiplicar.clicked.connect(self.producto)
        self.dividir.clicked.connect(self.division)
        
        sumarAct = QAction(QIcon('sumar.png'),'Sumar', self)
        sumarAct.setStatusTip('Sumar variables')
        sumarAct.setShortcut('Ctrl+S')
        sumarAct.triggered.connect(self.suma)
        
        restarAct = QAction(QIcon('restar.png'),'Restar', self)
        restarAct.setStatusTip('Restar variables')
        restarAct.setShortcut('Ctrl+R')
        restarAct.triggered.connect(self.resta)
        
        multiplicarAct = QAction(QIcon('multiplica.png'),'Multiplicar', self)
        multiplicarAct.setStatusTip('Multiplicar variables')
        multiplicarAct.setShortcut('Ctrl+M')
        multiplicarAct.triggered.connect(self.producto)
        
        dividirAct = QAction(QIcon('dividir.png'),'Dividir', self)
        dividirAct.setStatusTip('Dividir variables')
        dividirAct.setShortcut('Ctrl+D')
        dividirAct.triggered.connect(self.division)
        
        exitAct = QAction(QIcon('salir.png'), 'Salir', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Salir de la calculadora')
        exitAct.triggered.connect(self.close)        
        
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(sumarAct)
        fileMenu.addAction(restarAct)
        fileMenu.addAction(multiplicarAct)
        fileMenu.addAction(dividirAct)
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Salir')
        toolbar.addAction(sumarAct)
        toolbar.addAction(restarAct)
        toolbar.addAction(multiplicarAct)
        toolbar.addAction(dividirAct)
        toolbar.addAction(exitAct)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Calculadora')
        self.setWindowIcon(QIcon('calculadoraLogo.png'))
        self.show()
        
    def suma(self):
        respuesta = float(self.variable1.text()) + float(self.variable2.text())
        self.resultado.setText(str(respuesta))
        
    def resta(self):
        respuesta = float(self.variable1.text()) - float(self.variable2.text())
        self.resultado.setText(str(respuesta))
        
    def producto(self):
        respuesta = float(self.variable1.text()) * float(self.variable2.text())
        self.resultado.setText(str(respuesta))
        
    def division(self):
        respuesta = float(self.variable1.text()) / float(self.variable2.text())
        self.resultado.setText(str(respuesta))
        
def main():
   
    calcu = calculadora()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()