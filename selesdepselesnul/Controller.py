from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from selesdepselesnul.Parser import RpnParser

# author : Moch Deden (https://github.com/selesdepelesnul)
class MainWindowController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('selesdepselesnul/main.ui', self)
        self.ui.infix_expr_line_edit.editingFinished.connect(
            self.on_editing_finished)

    def on_editing_finished(self):
        parser = RpnParser(self.ui.infix_expr_line_edit.text())
        parsed_list = parser.parse()

        self.ui.postfix_expr_line_edit.clear()
        if parsed_list != []:
            self.ui.postfix_expr_line_edit.setText(str(parsed_list))
        else:
            invalid_message_box = QMessageBox()
            invalid_message_box.setText('Expressi yang dimasukan tidak valid!')
            invalid_message_box.exec_()
