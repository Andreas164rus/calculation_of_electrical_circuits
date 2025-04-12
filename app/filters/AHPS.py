from PyQt5 import QtCore, QtGui, QtWidgets

from utils import prefix_converter

from math import pi, atan, log10


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1070, 597)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 380, 501, 151))
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
        self.Gain = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gain.sizePolicy().hasHeightForWidth())
        self.Gain.setSizePolicy(sizePolicy)
        self.Gain.setMinimumSize(QtCore.QSize(0, 30))
        self.Gain.setObjectName("Gain")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Gain)
        self.Gain_db = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gain_db.sizePolicy().hasHeightForWidth())
        self.Gain_db.setSizePolicy(sizePolicy)
        self.Gain_db.setMinimumSize(QtCore.QSize(0, 30))
        self.Gain_db.setObjectName("Gain_db")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Gain_db)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.Fc = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fc.sizePolicy().hasHeightForWidth())
        self.Fc.setSizePolicy(sizePolicy)
        self.Fc.setMinimumSize(QtCore.QSize(0, 30))
        self.Fc.setObjectName("Fc")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Fc)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 511, 234))
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
        self.F_in = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F_in.sizePolicy().hasHeightForWidth())
        self.F_in.setSizePolicy(sizePolicy)
        self.F_in.setMinimumSize(QtCore.QSize(0, 30))
        self.F_in.setObjectName("F_in")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.F_in)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.C1 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C1.sizePolicy().hasHeightForWidth())
        self.C1.setSizePolicy(sizePolicy)
        self.C1.setMinimumSize(QtCore.QSize(0, 30))
        self.C1.setObjectName("C1")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.C1)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.R1 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R1.sizePolicy().hasHeightForWidth())
        self.R1.setSizePolicy(sizePolicy)
        self.R1.setMinimumSize(QtCore.QSize(0, 30))
        self.R1.setObjectName("R1")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.R1)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.R2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R2.sizePolicy().hasHeightForWidth())
        self.R2.setSizePolicy(sizePolicy)
        self.R2.setMinimumSize(QtCore.QSize(0, 30))
        self.R2.setObjectName("R2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.R2)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.R3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R3.sizePolicy().hasHeightForWidth())
        self.R3.setSizePolicy(sizePolicy)
        self.R3.setMinimumSize(QtCore.QSize(0, 30))
        self.R3.setObjectName("R3")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.R3)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(540, 80, 511, 451))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../img/filters/AHPS.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(380, 30, 47, 13))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.R1.setValidator(QtGui.QDoubleValidator())
        self.R2.setValidator(QtGui.QDoubleValidator())
        self.R3.setValidator(QtGui.QDoubleValidator())
        self.C1.setValidator(QtGui.QDoubleValidator())
        self.F_in.setValidator(QtGui.QDoubleValidator())
        self.Gain.setValidator(QtGui.QDoubleValidator())
        self.Gain_db.setValidator(QtGui.QDoubleValidator())
        self.Fc.setValidator(QtGui.QDoubleValidator())

        self.pushButton.clicked.connect(self.calculate)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Усиление"))
        self.label_5.setText(_translate("Form", "Усиление, дб"))
        self.label_10.setText(_translate("Form", "Частота среза, Гц"))
        self.label.setText(_translate("Form", "Входная частота, Гц"))
        self.label_3.setText(_translate("Form", "Емкость C1, мкФ"))
        self.pushButton.setText(_translate("Form", "Расчитать"))
        self.label_8.setText(_translate("Form", "Сопротивлеление резистора R1, Ом"))
        self.label_9.setText(_translate("Form", "Сопротивлеление резистора R2, Ом"))
        self.label_11.setText(_translate("Form", "Сопротивлеление резистора R3, Ом"))

    def calculate(self):
        R1 = float(self.R1.text().replace(',', '.'))
        R2 = float(self.R2.text().replace(',', '.'))
        R3 = float(self.R3.text().replace(',', '.'))
        C1 = float(self.C1.text().replace(',', '.')) * 1e-6
        F_in = float(self.F_in.text().replace(',', '.'))

        Fc = (2 * pi * R3 * C1)**-1
        Gain = (1 + R2/R1) * (F_in / Fc) / (1 + (F_in / Fc)**2) ** 0.5
        Gain_db = 20 * log10(Gain)

        self.Fc.setText(prefix_converter(Fc).replace(',','.'))
        self.Gain.setText(prefix_converter(Gain).replace(',','.'))
        self.Gain_db.setText(prefix_converter(Gain_db).replace(',','.'))
