from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.resize(800, 600)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(430, 520, 341, 32))

        self.textEdit = QtWidgets.QLineEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(60, 110, 291, 41))

        self.textEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 190, 291, 41))

        self.textEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(60, 270, 291, 41))

        self.textEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(70, 440, 201, 41))

        self.textEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(490, 440, 201, 41))

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.file)
        self.pushButton.setText("Analizar")
        self.pushButton.setGeometry(QtCore.QRect(300, 380, 121, 41))

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 390, 191, 41))
        self.label.setText("Número de vocales")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(470, 390, 241, 21))
        self.label_2.setText("Número de consonantes")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(410, 110, 201, 41))
        self.label_3.setText("Nombre del archivo")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(410, 190, 161, 41))
        self.label_4.setText("Texto a escribir")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(410, 270, 171, 41))
        self.label_5.setText("Número de líneas")

    def file(self):
        nombre = self.textEdit.text()
        texto = self.textEdit_2.text()
        num = int(self.textEdit_3.text())
        f = open(nombre, 'w')
        i = 0
        while (i<num):
            f.write(nombre)
            i += 1
        j = 0
        for c in texto:
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                j += 1
        con = len(texto.replace(" ", "")) - j
        f.close()

        self.textEdit_4.setText(str(j*num))
        self.textEdit_5.setText(str(con*num))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
