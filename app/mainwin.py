from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 727)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bossters = QtWidgets.QComboBox(self.layoutWidget)
        self.bossters.setEnabled(True)
        self.bossters.setObjectName("bossters")
        self.bossters.addItem("")
        self.bossters.addItem("")
        self.bossters.addItem("")
        self.horizontalLayout.addWidget(self.bossters)
        self.converters = QtWidgets.QComboBox(self.layoutWidget)
        self.converters.setObjectName("converters")
        self.converters.addItem("")
        self.converters.addItem("")
        self.horizontalLayout.addWidget(self.converters)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bossters.setItemText(0, _translate("MainWindow", "Усилители"))
        self.bossters.setItemText(1, _translate("MainWindow", "А_класс ОЭ 1"))
        self.bossters.setItemText(2, _translate("MainWindow", "А_класс ОЭ 2"))
        self.converters.setItemText(0, _translate("MainWindow", "Преобразователи"))
        self.converters.setItemText(1, _translate("MainWindow", "Повышающий"))
