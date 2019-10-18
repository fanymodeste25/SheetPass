# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from fichier.fusion import fusionSheet

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fusionSheet()
    ui.showMaximized()
    sys.exit(app.exec_())

