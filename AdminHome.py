

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminHome(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 467)
        Dialog.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 110, 211, 41))
        self.pushButton.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 210, 211, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 110, 211, 41))
        self.pushButton_3.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 210, 211, 41))
        self.pushButton_4.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 300, 211, 41))
        self.pushButton_5.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AdminHome"))
        self.pushButton.setText(_translate("Dialog", "Image Acquisition"))
        self.pushButton_2.setText(_translate("Dialog", "Low Resolution Images"))
        self.pushButton_3.setText(_translate("Dialog", "Histogram Equalization"))
        self.pushButton_4.setText(_translate("Dialog", "Adaptive HE"))
        self.pushButton_5.setText(_translate("Dialog", "Interpolation"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
