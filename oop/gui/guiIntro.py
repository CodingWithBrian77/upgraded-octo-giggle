# PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(400, 150, 500, 500)
        self.setWindowIcon(QIcon("oop/gui/220984061.png"))

def main():
    app = QApplication(sys.argv) # allows PyQt to process any command line arguments intended for it
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
