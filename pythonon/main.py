import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QShortcut
from PyQt5.QtGui import QKeySequence



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('HAWAI.ui', self)
        self.Save_btn.clicked.connect(self.Save_btn_did)
        self.Open_btn.clicked.connect(self.Open_btn_did)
        self.Change_btn.clicked.connect(self.Change_btn_did)
        self.Change_key = QShortcut(QKeySequence('Ctrl+S'), self)
        self.Change_key.activated.connect(self.Change_btn_did)
        self.path_lable.setText('Путь')

        self.proverka_puti = None   #Ты думал тут что-то будет, НЕТ

    def Save_btn_did(self):
        try:
            filename = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")[0]
            text_file = self.textEdit.toPlainText()
            with open(filename, 'w') as fuck_3:
                fuck_3.write(text_file)
            self.proverka_puti = filename
            self.path_lable.setText(self.proverka_puti)

        except FileNotFoundError:
            print('Выбери файл')

    def Open_btn_did(self):
        try:
            filename = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")[0]
            with open(filename, 'r') as fuck:
                text_file = fuck.read()
                self.textEdit.setText(text_file)
            self.proverka_puti = filename
            self.path_lable.setText(self.proverka_puti)
        except FileNotFoundError:
            print('Выбери файл')

    def Change_btn_did(self):
        if self.proverka_puti is not None:
            text_file = self.textEdit.toPlainText()
            with open(self.proverka_puti, 'w') as fuck_2:
                fuck_2.write(text_file)
        else:
            self.Save_btn_did()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hren = App()
    hren.show()
    sys.exit(app.exec())
