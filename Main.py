

from PyQt5 import QtCore, QtGui, QtWidgets
from Admin import Ui_Admin

class Ui_Main(object):

    def __init__(self, Dialog):
        self.dialog = Dialog

    def adminlogin(self, event):
        try:
            self.admn = QtWidgets.QDialog()
            self.ui = Ui_Admin(self.admn)
            self.ui.setupUi(self.admn)
            self.admn.show()
            self.dialog.hide()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 448)
        Dialog.setStyleSheet("background-color: rgb(116, 58, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 721, 51))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"Vani\";")
        self.label.setObjectName("label")
        self.admin = QtWidgets.QLabel(Dialog)
        self.admin.setGeometry(QtCore.QRect(150, 170, 301, 181))
        self.admin.setStyleSheet("image: url(admin.png);")
        self.admin.setText("")
        self.admin.setObjectName("admin")
        self.admin.mousePressEvent = self.adminlogin
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 80, 911, 51))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Vani\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.label.setText(_translate("Dialog", "Interpolation of the Histogramed MR Brain"))
        self.label_3.setText(_translate("Dialog", "Images for Resolution Enhancement"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
