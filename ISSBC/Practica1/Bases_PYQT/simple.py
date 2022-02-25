#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:29:44 2022

@author: jose
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv) 

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
