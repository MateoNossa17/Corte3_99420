import sys
import PyQt5.QtWidgets as PyQT
from PyQt5 import uic
# Signal / Slot
# Elemento / accion 

class Principal(PyQT.QMainWindow):
    def __init__(self): 
        super().__init__()
        self.initGui()
    def initGui(self):
        uic.loadUi("primerejercicio.ui",self)
        self.show()
        self.pushButton.clicked.connect(self.calcular)
    def calcular(self):
        texto1=self.num1.text()
        texto2=self.num2.text()
        if self.opesuma.isChecked()==True:
            sum=float(texto1)+float(texto2)
            self.resultado.setText(str(sum))
        elif self.operesta.isChecked()==True:
            res=float(texto1)-float(texto2)
            self.resultado.setText(str(res))
        elif self.opedividir.isChecked()==True:
            divi=float(texto1)/float(texto2)
            self.resultado.setText(str(divi))
        else:
            mul=float(texto1)*float(texto2)
            self.resultado.setText(str(mul))
def main():
    app=PyQT.QApplication([])
    window= Principal()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()


