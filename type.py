import sys

import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtCore import Slot

from LED import text


class type(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Initialize the UserInterface, set up the layout, and create necessary widgets.
        """
        super().__init__()

        # Central widget and layout
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # PyQtGraph global settings
        pg.setConfigOption("background", "w")
        pg.setConfigOption("foreground", "k")

        vbox = QtWidgets.QVBoxLayout(central_widget)
        self.ask_text = QtWidgets.QLineEdit()
        vbox.addWidget(self.ask_text)
        self.ask_text.returnPressed.connect(self.app)

    @Slot()
    def app(self):
        appje = self.ask_text.text()
        tex = text()
        print(appje)
        tex.morse(appje)


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = type()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
