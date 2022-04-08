# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(294, 363)
        self.OptionsGroup = QtWidgets.QGroupBox(Form)
        self.OptionsGroup.setGeometry(QtCore.QRect(10, 10, 271, 341))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.OptionsGroup.setFont(font)
        self.OptionsGroup.setObjectName("OptionsGroup")
        self.threadLbl = QtWidgets.QLabel(self.OptionsGroup)
        self.threadLbl.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.threadLbl.setObjectName("threadLbl")
        self.threadCountSpin = QtWidgets.QSpinBox(self.OptionsGroup)
        self.threadCountSpin.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.threadCountSpin.setObjectName("threadCountSpin")
        self.passphraseLengthLbl = QtWidgets.QLabel(self.OptionsGroup)
        self.passphraseLengthLbl.setGeometry(QtCore.QRect(20, 80, 211, 31))
        self.passphraseLengthLbl.setObjectName("passphraseLengthLbl")
        self.passphraseMaxLenSpin = QtWidgets.QSpinBox(self.OptionsGroup)
        self.passphraseMaxLenSpin.setGeometry(QtCore.QRect(20, 120, 81, 21))
        self.passphraseMaxLenSpin.setObjectName("passphraseMaxLenSpin")
        self.maxBruteForceLenLbl = QtWidgets.QLabel(self.OptionsGroup)
        self.maxBruteForceLenLbl.setGeometry(QtCore.QRect(20, 150, 211, 31))
        self.maxBruteForceLenLbl.setObjectName("maxBruteForceLenLbl")
        self.bruteForceMaxSpin = QtWidgets.QSpinBox(self.OptionsGroup)
        self.bruteForceMaxSpin.setGeometry(QtCore.QRect(20, 190, 81, 21))
        self.bruteForceMaxSpin.setObjectName("bruteForceMaxSpin")
        self.applyOptionsBtn = QtWidgets.QPushButton(self.OptionsGroup)
        self.applyOptionsBtn.setGeometry(QtCore.QRect(10, 300, 251, 31))
        self.applyOptionsBtn.setObjectName("applyOptionsBtn")
        self.minBruteForceLenLbl = QtWidgets.QLabel(self.OptionsGroup)
        self.minBruteForceLenLbl.setGeometry(QtCore.QRect(20, 220, 211, 31))
        self.minBruteForceLenLbl.setObjectName("minBruteForceLenLbl")
        self.bruteForceMinSpin = QtWidgets.QSpinBox(self.OptionsGroup)
        self.bruteForceMinSpin.setGeometry(QtCore.QRect(20, 250, 81, 21))
        self.bruteForceMinSpin.setObjectName("bruteForceMinSpin")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.OptionsGroup.setTitle(_translate("Form", "Options"))
        self.threadLbl.setText(_translate("Form", "Threads:"))
        self.passphraseLengthLbl.setText(_translate("Form", "Passphrase MAX Length:"))
        self.maxBruteForceLenLbl.setText(_translate("Form", "Max Brute Force length"))
        self.applyOptionsBtn.setText(_translate("Form", "Apply"))
        self.minBruteForceLenLbl.setText(_translate("Form", "Min Brute Force length"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())