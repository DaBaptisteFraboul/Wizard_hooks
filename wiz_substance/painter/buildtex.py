import subprocess
import os
import sys

from PyQt5 import QtWidgets

def get_env():
    for variable in os.environ:
        print(variable, os.environ[variable])

def buildtex_window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow(app)
    app.setFixedSize(600, 600)
    app.setWindowTitle("Export Buildtex")
    buton = QtWidgets.QPushButton("My button", parent=app)
    w.show()
    app.exec_()

def sub():
    process = subprocess.run(['guerilla'])