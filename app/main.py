from PyQt5 import QtWidgets
from mainwin import Ui_MainWindow
import sys

from boosters import a_class_1_form, a_class_2_form

value_bossters = {
    "А_класс ОЭ 1": a_class_1_form,
    "А_класс ОЭ 2": a_class_2_form
}

value_name = value_bossters


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bossters.currentTextChanged.connect(self.open_scheme)
        self.ui.converters.currentTextChanged.connect(self.open_scheme)
        self.now_widget = None
        self.left_margin = 0
        self.width_obj = 0
        self.showMaximized()
        self.height_window = self.size().height()
        for v in value_name.values():
            setattr(self, v.__name__, None)

    def open_scheme(self, value):
        class_ui = value_name.get(value)
        if class_ui:
            class_name = class_ui.__name__
        else:
            getattr(self, self.now_widget.__name__).deleteLater()
            setattr(self, self.now_widget.__name__, None)
            self.ui.bossters.setCurrentIndex(0)
            return

        if getattr(self, class_name):
            getattr(self, class_name).deleteLater()
            setattr(self, class_name, None)
        setattr(self, class_name, QtWidgets.QWidget())
        self.form_ui = value_name.get(value)()
        self.form_ui.setupUi(getattr(self, class_name))
        getattr(self, class_name).setParent(self)
        getattr(self, class_name).show()
        self.width_window = self.size().width()
        self.width_obj = getattr(self, class_name).size().width()
        self.left_margin = (self.width_window - self.width_obj)//2
        getattr(self, class_name).move(self.left_margin, 30)
        self.now_widget = value_name.get(value)

    def resizeEvent(self, event):
        if self.now_widget:
            self.old_width = self.width_window
            self.width_window = self.size().width()
            self.height_window = self.size().height()
            self.delta_width = self.width_window - self.width_obj
            getattr(self, self.now_widget.__name__).move(abs(self.delta_width//2), 30)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
