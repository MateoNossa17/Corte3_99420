import sys
import PyQt5.QtWidgets as PyQT
from PyQt5.QtCore import Qt
from PyQt5 import uic

class AgregarEsView(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.inagre()
    def inagre(self):
        uic.loadUi('agrgarmateria.ui', self)
        self.show()
        self.agregarno.clicked.connect(lambda: self.calno())
        self.err_code.setVisible(False)
        self.err_ma.setVisible(False)
        self.err_notes.setVisible(False)


    def calno(self):
        self.err_code.setVisible(False)
        self.err_ma.setVisible(False)
        self.err_notes.setVisible(False)

        try:
            codies = int(self.codiestu.text())
        
        except ValueError:
            self.err_code.setVisible(True)
            return

        mate = self.matees.text()

        if mate == "":
            self.err_ma.setVisible(True)
            return

        try:
            labo = float(self.lab.text())
            Proy = float(self.pro.text())
            Parc = float(self.par.text())

        except ValueError:
            self.err_notes.setVisible(True)
            return

        if self.corte1.isChecked():
            note = (labo*(1/3))+(Proy*1/3)+(Parc*1/3)
            court = 1

        elif self.corte2.isChecked():
            note = (labo*(1/3))+(Proy*1/3)+(Parc*1/3)
            court = 2

        else:
            note = (labo*(1/4))+(Proy*1/4)+(Parc*2/4)
            court = 3

        self.notac.setText(str(round(note,1)))
        
def main():
    app = PyQT.QApplication([])
    window = AgregarEsView()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()