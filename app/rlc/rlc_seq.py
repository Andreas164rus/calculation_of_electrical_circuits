from PyQt5 import QtCore, QtGui, QtWidgets

from utils import prefix_converter

import math


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1070, 597)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 370, 501, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.Freq_hz = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Freq_hz.sizePolicy().hasHeightForWidth())
        self.Freq_hz.setSizePolicy(sizePolicy)
        self.Freq_hz.setMinimumSize(QtCore.QSize(0, 30))
        self.Freq_hz.setObjectName("Freq_hz")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Freq_hz)
        self.Freq_rad = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Freq_rad.sizePolicy().hasHeightForWidth())
        self.Freq_rad.setSizePolicy(sizePolicy)
        self.Freq_rad.setMinimumSize(QtCore.QSize(0, 30))
        self.Freq_rad.setObjectName("Freq_rad")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Freq_rad)
        self.QQ = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QQ.sizePolicy().hasHeightForWidth())
        self.QQ.setSizePolicy(sizePolicy)
        self.QQ.setMinimumSize(QtCore.QSize(0, 30))
        self.QQ.setObjectName("QQ")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.QQ)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.ZZ = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZZ.sizePolicy().hasHeightForWidth())
        self.ZZ.setSizePolicy(sizePolicy)
        self.ZZ.setMinimumSize(QtCore.QSize(0, 30))
        self.ZZ.setObjectName("ZZ")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ZZ)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 511, 151))
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
        self.RR = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RR.sizePolicy().hasHeightForWidth())
        self.RR.setSizePolicy(sizePolicy)
        self.RR.setMinimumSize(QtCore.QSize(0, 30))
        self.RR.setObjectName("RR")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.RR)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.LL = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LL.sizePolicy().hasHeightForWidth())
        self.LL.setSizePolicy(sizePolicy)
        self.LL.setMinimumSize(QtCore.QSize(0, 30))
        self.LL.setObjectName("LL")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LL)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.CC = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CC.sizePolicy().hasHeightForWidth())
        self.CC.setSizePolicy(sizePolicy)
        self.CC.setMinimumSize(QtCore.QSize(0, 30))
        self.CC.setObjectName("CC")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.CC)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(540, 80, 511, 451))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../img/RLC/RLC_seq.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(380, 30, 47, 13))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.RR.setValidator(QtGui.QDoubleValidator())
        self.LL.setValidator(QtGui.QDoubleValidator())
        self.CC.setValidator(QtGui.QDoubleValidator())
        self.Freq_hz.setValidator(QtGui.QDoubleValidator())
        self.Freq_rad.setValidator(QtGui.QDoubleValidator())
        self.QQ.setValidator(QtGui.QDoubleValidator())
        self.ZZ.setValidator(QtGui.QDoubleValidator())
        # self.Re.setValidator(QtGui.QDoubleValidator())

        self.pushButton.clicked.connect(self.calculate)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Резонансная частота, рад/с"))
        self.label_4.setText(_translate("Form", "Резонсная частота, Гц"))
        self.label_10.setText(_translate("Form", "Добротность"))
        self.label_11.setText(_translate("Form", "Импеданс, Ом"))
        self.label.setText(_translate("Form", "Сопроивление резистора R, Ом"))
        self.label_2.setText(_translate("Form", "Индуктивность L, мГн"))
        self.label_3.setText(_translate("Form", "Емкость C, мкФ"))
        self.pushButton.setText(_translate("Form", "Расчитать"))

    def calculate(self):
        RR = float(self.RR.text().replace(',', '.'))
        LL = float(self.LL.text().replace(',', '.')) / 1e3
        CC = float(self.CC.text().replace(',', '.')) / 1e6
        Freq_rad = 1/(LL*CC)**0.5
        Freq_hz = Freq_rad / (2 * math.pi)
        QQ = 2 * math.pi * Freq_hz * LL / RR
        XL = 2j*math.pi*Freq_hz*LL
        XC = 1j/(2*math.pi*Freq_hz*CC)
        ZZ = RR + XL - XC
        self.Freq_hz.setText(prefix_converter(Freq_hz).replace(',','.'))
        self.Freq_rad.setText(prefix_converter(Freq_rad).replace(',','.'))
        self.QQ.setText(prefix_converter(QQ).replace(',','.'))
        self.ZZ.setText(f"{ZZ}")
