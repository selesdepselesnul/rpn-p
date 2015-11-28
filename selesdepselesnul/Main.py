from PyQt5.QtWidgets import QApplication
import sys
from selesdepselesnul.Controller import MainWindowController

# author : Moch Deden (https://github.com/selesdepelesnul)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window_controller = MainWindowController()
    main_window_controller.show()
    main_window_controller.setFixedWidth(359)
    main_window_controller.setFixedHeight(165)
    main_window_controller.setWindowTitle('RPN-P')
    sys.exit(app.exec_())
