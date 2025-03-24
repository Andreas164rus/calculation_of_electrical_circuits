from PyQt5 import QtWidgets
from mainwin import Ui_MainWindow
import sys

from boosters import a_class_1_form, a_class_2_form
from rlc import rlc_seq_form, rlc_par_form, LPF_form
from operationals import invert_form, neinvert_form

value_bossters = {
    "А_класс ОЭ 1": a_class_1_form,
    "А_класс ОЭ 2": a_class_2_form,
    "Последовательный RLC": rlc_seq_form,
    "Параллельный RLC": rlc_par_form,
    "Инверт включение": invert_form,
    "Неинверт включение": neinvert_form,
    "ФНЧ": LPF_form,
}


value_name = value_bossters


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.select_head = [self.ui.bossters, self.ui.rlc, self.ui.opetaionals]
        for select in self.select_head:
            select.currentTextChanged.connect(self.open_scheme)
        self.now_widget = None
        self.left_margin = 0
        self.width_obj = 0
        self.showMaximized()
        self.head_now = None
        self.height_window = self.size().height()

        for v in value_name.values():
            setattr(self, v.__name__, None)

    def open_scheme(self, value):
        class_ui = value_name.get(value)
        if self.head_now:
            for select in self.select_head:
                if self.sender() != select:
                    select.blockSignals(True)
                    select.setCurrentIndex(0)
                    select.blockSignals(False)
        if class_ui:
            self.head_now = True
            class_name = class_ui.__name__
        else:
            if getattr(self, self.now_widget.__name__):
                getattr(self, self.now_widget.__name__).deleteLater()
                setattr(self, self.now_widget.__name__, None)
            for select in self.select_head:
                select.setCurrentIndex(0)
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
