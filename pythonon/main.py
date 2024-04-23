import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QFile



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('HAWAI.ui', self)
        self.Save_btn.clicked.connect(self.Save_btn_did)
        self.Open_btn.clicked.connect(self.Open_btn_did)
        self.Change_btn.clicked.connect(self.Change_btn_did)

        self.proverka_puti = None   #Ты думал тут что-то будет, НЕТ

    def Save_btn_did(self):
        if self.proverka_puti != None:
            text_file = self.textEdit.toPlainText()
            print(self.proverka_puti)
            with open(self.proverka_puti, 'w') as fuck_2:
                fuck_2.write(text_file)
        else:
            print('абоба')

    def Open_btn_did(self):
        filename = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")[0]
        with open(filename, 'r') as fuck:
            text_file = fuck.read()
            self.textEdit.setText(text_file)
        self.proverka_puti = filename


    def Change_btn_did(self):
        print('Нет')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    hren = App()
    hren.show()
    sys.exit(app.exec())