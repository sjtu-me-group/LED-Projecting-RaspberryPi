import sys
import time
from PyQt5 import QtWidgets,QtCore
import data

resolution_x = 800
resolution_y = 600
gl = 20


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.name_label = QtWidgets.QLabel(self)
        self.comboBox = QtWidgets.QComboBox(self)
        self.work_label = QtWidgets.QLabel(self)
        self.print_button = QtWidgets.QPushButton(self)
        self.combo_refresh_button = QtWidgets.QPushButton(self)
        self.timer_200ms = QtCore.QTimer(self)
        self.timer_refresh = QtCore.QTimer(self)

        self.create_window()

    def create_window(self):
        self.resize(resolution_x, resolution_y)
        self.setWindowTitle("控制中心")

        self.name_label.setGeometry(gl*31, gl*5, gl*6, gl*1)
        self.name_label.setText("请选择人员:")

        self.comboBox.setGeometry(QtCore.QRect(gl * 31, gl*6, gl*6, gl*1.5))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.clear()
        self.comboBox.addItem('请选择')

        self.work_label.setGeometry(gl * 5, gl*10, gl*20, gl*15)

        self.print_button.setGeometry(gl * 32, gl * 22, gl * 4, gl * 3)
        self.print_button.setText("打印")
        self.print_button.clicked.connect(self.print_clicked)

        self.combo_refresh_button.setGeometry(gl * 31, gl * 2, gl * 5, gl * 2)
        self.combo_refresh_button.setText("刷新")
        self.combo_refresh_button.clicked.connect(self.combo_refresh)

        self.timer_200ms.start(200)

        self.timer_refresh.start(30000)
        self.timer_refresh.timeout.connect(self.combo_refresh)

        self.show()

    def combo_refresh(self):
        print("combo_refresh")
        self.comboBox.clear()
        for k, v in data.data.items():
            self.comboBox.addItem(k, v)

    def print_clicked(self):
        print("print")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
