# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a_class_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1070, 597)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 310, 491, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Rc = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.Rc.setMaximumSize(QtCore.QSize(100, 30))
        self.Rc.setObjectName("Rc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Rc)
        self.Rb = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.Rb.setMaximumSize(QtCore.QSize(100, 30))
        self.Rb.setObjectName("Rb")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Rb)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 90, 478, 173))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Ein = QtWidgets.QPlainTextEdit(self.formLayoutWidget_2)
        self.Ein.setMaximumSize(QtCore.QSize(100, 30))
        self.Ein.setObjectName("Ein")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Ein)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Ic = QtWidgets.QPlainTextEdit(self.formLayoutWidget_2)
        self.Ic.setMaximumSize(QtCore.QSize(100, 30))
        self.Ic.setObjectName("Ic")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Ic)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.Ube = QtWidgets.QPlainTextEdit(self.formLayoutWidget_2)
        self.Ube.setMaximumSize(QtCore.QSize(100, 30))
        self.Ube.setObjectName("Ube")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Ube)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.h21 = QtWidgets.QPlainTextEdit(self.formLayoutWidget_2)
        self.h21.setMaximumSize(QtCore.QSize(100, 30))
        self.h21.setObjectName("h21")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.h21)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(540, 80, 511, 451))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../img/boosters/a_class_2.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(380, 30, 47, 13))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Сопротивление коллекторного резистора"))
        self.label_5.setText(_translate("Form", "Сопротивление базового резистора"))
        self.label.setText(_translate("Form", "Напряжения истоника питания"))
        self.label_2.setText(_translate("Form", "Ток коллектора"))
        self.label_3.setText(_translate("Form", "Переход База-Эмиттер"))
        self.pushButton.setText(_translate("Form", "Расчитать"))
        self.label_8.setText(_translate("Form", "Коэффициент усиления (h21э)"))
