import sys
from PyQt5 import QtWidgets

resolution_x = 800
resolution_y = 600
gl = 20


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.create_window()

    def create_window(self):
        self.resize(resolution_x, resolution_y)
        self.setWindowTitle("控制中心")
        print_button = QtWidgets.QPushButton(self)
        print_button.setGeometry(gl * 32, gl * 22, gl * 4, gl * 3)
        print_button.setText("打印")
        print_button.clicked.connect(self.print_clicked)
        self.show()

    def print_clicked(self):
        print("print")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())