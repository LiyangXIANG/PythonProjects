# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(301, 308)
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(20, 140, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton1.setFont(font)
        self.pushButton1.setAutoFillBackground(False)
        self.pushButton1.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(60, 140, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setAutoFillBackground(False)
        self.pushButton2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(Form)
        self.pushButton3.setGeometry(QtCore.QRect(100, 140, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton3.setFont(font)
        self.pushButton3.setAutoFillBackground(False)
        self.pushButton3.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton4 = QtWidgets.QPushButton(Form)
        self.pushButton4.setGeometry(QtCore.QRect(140, 140, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton4.setFont(font)
        self.pushButton4.setAutoFillBackground(False)
        self.pushButton4.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton5 = QtWidgets.QPushButton(Form)
        self.pushButton5.setGeometry(QtCore.QRect(20, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton5.setFont(font)
        self.pushButton5.setAutoFillBackground(False)
        self.pushButton5.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton6 = QtWidgets.QPushButton(Form)
        self.pushButton6.setGeometry(QtCore.QRect(60, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton6.setFont(font)
        self.pushButton6.setAutoFillBackground(False)
        self.pushButton6.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton7 = QtWidgets.QPushButton(Form)
        self.pushButton7.setGeometry(QtCore.QRect(100, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton7.setFont(font)
        self.pushButton7.setAutoFillBackground(False)
        self.pushButton7.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton8 = QtWidgets.QPushButton(Form)
        self.pushButton8.setGeometry(QtCore.QRect(140, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton8.setFont(font)
        self.pushButton8.setAutoFillBackground(False)
        self.pushButton8.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton8.setObjectName("pushButton8")
        self.pushButton9 = QtWidgets.QPushButton(Form)
        self.pushButton9.setGeometry(QtCore.QRect(20, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton9.setFont(font)
        self.pushButton9.setAutoFillBackground(False)
        self.pushButton9.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton9.setObjectName("pushButton9")
        self.pushButton0 = QtWidgets.QPushButton(Form)
        self.pushButton0.setGeometry(QtCore.QRect(60, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton0.setFont(font)
        self.pushButton0.setAutoFillBackground(False)
        self.pushButton0.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton0.setObjectName("pushButton0")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 261, 111))
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textEdit.setFont(font)

        self.pushButton_point = QtWidgets.QPushButton(Form)
        self.pushButton_point.setGeometry(QtCore.QRect(100, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_point.setFont(font)
        self.pushButton_point.setAutoFillBackground(False)
        self.pushButton_point.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton_point.setObjectName("pushButton_point")
        self.pushButton_clear = QtWidgets.QPushButton(Form)
        self.pushButton_clear.setGeometry(QtCore.QRect(100, 260, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #f6e3bd;\n"
"border:2px solid black;\n"
"}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_per = QtWidgets.QPushButton(Form)
        self.pushButton_per.setGeometry(QtCore.QRect(140, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_per.setFont(font)
        self.pushButton_per.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #bdeff6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton_per.setObjectName("pushButton_per")
        self.pushButton_back = QtWidgets.QPushButton(Form)
        self.pushButton_back.setGeometry(QtCore.QRect(20, 260, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #f6e3bd;\n"
"border:2px solid black;\n"
"}")
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_square = QtWidgets.QPushButton(Form)
        self.pushButton_square.setGeometry(QtCore.QRect(230, 140, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_square.setFont(font)
        self.pushButton_square.setAutoFillBackground(True)
        self.pushButton_square.setStyleSheet("QPushButton\n"
"{\n"
"border:2px solid black;\n"
"}")
        self.pushButton_square.setObjectName("pushButton_square")

        self.pushButton_tri = QtWidgets.QPushButton(Form)
        self.pushButton_tri.setGeometry(QtCore.QRect(230, 180, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_tri.setFont(font)
        self.pushButton_tri.setAutoFillBackground(True)
        self.pushButton_tri.setStyleSheet("QPushButton\n"
                                             "{\n"
                                             "border:2px solid black;\n"
                                             "}")
        self.pushButton_tri.setObjectName("pushButton_tri")

        self.pushButton_sqrt = QtWidgets.QPushButton(Form)
        self.pushButton_sqrt.setGeometry(QtCore.QRect(230, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_sqrt.setAutoFillBackground(True)
        self.pushButton_sqrt.setStyleSheet("QPushButton\n"
                                          "{\n"
                                          "border:2px solid black;\n"
                                          "}")
        self.pushButton_sqrt.setFont(font)
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")

        self.pushButton_n = QtWidgets.QPushButton(Form)
        self.pushButton_n.setGeometry(QtCore.QRect(60, 260, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_n.setFont(font)
        self.pushButton_n.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #f6e3bd;\n"
"border:2px solid black;\n"
"}")
        self.pushButton_n.setObjectName("pushButton_n")
        self.pushButton_plus = QtWidgets.QPushButton(Form)
        self.pushButton_plus.setGeometry(QtCore.QRect(190, 140, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #f5bdf6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_minus = QtWidgets.QPushButton(Form)
        self.pushButton_minus.setGeometry(QtCore.QRect(190, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #f5bdf6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_multiply = QtWidgets.QPushButton(Form)
        self.pushButton_multiply.setGeometry(QtCore.QRect(190, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_multiply.setFont(font)
        self.pushButton_multiply.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #f5bdf6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_divide = QtWidgets.QPushButton(Form)
        self.pushButton_divide.setGeometry(QtCore.QRect(190, 260, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_divide.setFont(font)
        self.pushButton_divide.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #f5bdf6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_equal = QtWidgets.QPushButton(Form)
        self.pushButton_equal.setGeometry(QtCore.QRect(230, 260, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #f5bdf6;\n"
"border:2px solid black;\n"
"}")
        self.pushButton_equal.setObjectName("pushButton_equal")

        self.retranslateUi(Form)
        self.pushButton1.clicked.connect(Form.pushButton1_clicked)  # link event with button
        self.pushButton2.clicked.connect(Form.pushButton2_clicked)
        self.pushButton3.clicked.connect(Form.pushButton3_clicked)
        self.pushButton4.clicked.connect(Form.pushButton4_clicked)
        self.pushButton5.clicked.connect(Form.pushButton5_clicked)
        self.pushButton6.clicked.connect(Form.pushButton6_clicked)
        self.pushButton7.clicked.connect(Form.pushButton7_clicked)
        self.pushButton8.clicked.connect(Form.pushButton8_clicked)
        self.pushButton9.clicked.connect(Form.pushButton9_clicked)
        self.pushButton0.clicked.connect(Form.pushButton0_clicked)
        self.pushButton_point.clicked.connect(Form.pushButton_point_clicked)
        self.pushButton_back.clicked.connect(Form.pushButton_back_clicked)
        self.pushButton_per.clicked.connect(Form.pushButton_per_clicked)
        self.pushButton_n.clicked.connect(Form.pushButton_n_clicked)
        self.pushButton_clear.clicked.connect(Form.pushButton_clear_clicked)

        self.pushButton_plus.clicked.connect(Form.pushButton_plus_clicked)
        self.pushButton_minus.clicked.connect(Form.pushButton_minus_clicked)
        self.pushButton_multiply.clicked.connect(Form.pushButton_multiply_clicked)
        self.pushButton_divide.clicked.connect(Form.pushButton_divide_clicked)

        self.pushButton_square.clicked.connect(Form.pushButton_square_clicked)
        self.pushButton_tri.clicked.connect(Form.pushButton_tri_clicked)
        self.pushButton_sqrt.clicked.connect(Form.pushButton_sqrt_clicked)

        self.pushButton_equal.clicked.connect(Form.pushButton_equal_clicked)


        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "计算器"))
        self.pushButton1.setText(_translate("Form", "1"))
        self.pushButton2.setText(_translate("Form", "2"))
        self.pushButton3.setText(_translate("Form", "3"))
        self.pushButton4.setText(_translate("Form", "4"))
        self.pushButton5.setText(_translate("Form", "5"))
        self.pushButton6.setText(_translate("Form", "6"))
        self.pushButton7.setText(_translate("Form", "7"))
        self.pushButton8.setText(_translate("Form", "8"))
        self.pushButton9.setText(_translate("Form", "9"))
        self.pushButton0.setText(_translate("Form", "0"))
        self.pushButton_point.setText(_translate("Form", "."))
        self.pushButton_clear.setText(_translate("Form", "clear"))
        self.pushButton_per.setText(_translate("Form", "%"))
        self.pushButton_back.setText(_translate("Form", "<"))
        self.pushButton_square.setText(_translate("Form", "平方"))
        self.pushButton_tri.setText(_translate("Form", "立方"))
        self.pushButton_sqrt.setText(_translate("Form", "根号"))
        self.pushButton_n.setText(_translate("Form", "^"))
        self.pushButton_plus.setText(_translate("Form", "+"))
        self.pushButton_minus.setText(_translate("Form", "-"))
        self.pushButton_multiply.setText(_translate("Form", "*"))
        self.pushButton_divide.setText(_translate("Form", "/"))
        self.pushButton_equal.setText(_translate("Form", "="))
