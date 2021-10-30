import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculadora import *

class calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ui.Botzero.clicked.connect(lambda:self.press_it('0'))
        self.ui.Botum.clicked.connect(lambda:self.press_it('1'))
        self.ui.Botdois.clicked.connect(lambda:self.press_it('2'))
        self.ui.Bottreis.clicked.connect(lambda:self.press_it('3'))
        self.ui.Botquatro.clicked.connect(lambda:self.press_it('4'))
        self.ui.Botcinco.clicked.connect(lambda:self.press_it('5'))
        self.ui.Botseis.clicked.connect(lambda:self.press_it('6'))
        self.ui.Botsete.clicked.connect(lambda:self.press_it('7'))
        self.ui.Botoito.clicked.connect(lambda:self.press_it('8'))
        self.ui.Botnove.clicked.connect(lambda:self.press_it('9'))

        #botões das operações
        self.ui.Botac.clicked.connect(lambda:self.press_it('AC'))
        self.ui.Botc.clicked.connect(lambda:self.apagar())
        self.ui.Botdiv.clicked.connect(lambda:self.press_it('/'))
        self.ui.Botmult.clicked.connect(lambda:self.press_it('*'))
        self.ui.Botmenos.clicked.connect(lambda:self.press_it('-'))
        self.ui.Botmais.clicked.connect(lambda:self.press_it('+'))
        self.ui.Botigual.clicked.connect(lambda:self.igual())
        self.ui.Botmaismen.clicked.connect(lambda:self.posneg())
        self.ui.Botponto.clicked.connect(lambda:self.ponto())


        ## funcionalidades dos botões:

    def apagar(self) :
        tela = self.ui.visor.text()
        ##apagando o último número
        tela = tela[:-1]
        self.ui.visor.setText(tela)

    def press_it(self, pressed):
        tela = self.ui.visor.text()
        if len(tela) <= 7:
            if pressed == 'AC':
                self.ui.visor.setText('0')
            else:
                if self.ui.visor.text() == '0':
                    self.ui.visor.setText('')
                self.ui.visor.setText('{}{}'.format(self.ui.visor.text(), pressed))

    def igual(self):
        tela = self.ui.visor.text()
        try:
            ##saida da resposta
            resposta = eval(tela)
            self.ui.visor.setText (str(resposta))
        except:
            ##saida da msg de ERRO
            self.ui.visor.setText('Syntax ERROR')

            ## adicionando o positivo/negativo
    def posneg(self):
        tela = self.ui.visor.text()
        if '-' in tela:
            self.ui.visor.setText(tela.replace('-', ''))
        else:
            self.ui.visor.setText('-{}'.format(tela))

        ## adicionando o flutuante(float)
    def ponto(self):
        tela = self.ui.visor.text()
        if tela[-1] == '.':
            pass
        else:
            self.ui.visor.setText('{}.'.format(tela))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = calc()
    w.show()
    sys.exit(app.exec_())