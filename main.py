import sys
from PyQt5 import QtWidgets, QtCore
import data
# import LEDProjecting
# import serialPrinting

# 屏幕分辨率
resolution_x = 800
resolution_y = 480
# 网格长度
gl = 20
gly = 16


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        # 显示“请选择人员：”的简单提示性标签
        self.name_label = QtWidgets.QLabel(self)
        # 显示所有人员的下拉列表
        self.comboBox = QtWidgets.QComboBox(self)
        # 用来暂存data的数据
        self.data_copy = data.data
        # 显示下拉列表选中的人员的工作的标签
        self.work_label = QtWidgets.QLabel(self)
        # 按下此按钮后打印下拉列表选中人员的名字和工作
        self.print_button = QtWidgets.QPushButton(self)
        # 按下此按钮刷新人员下拉列表
        self.combo_refresh_button = QtWidgets.QPushButton(self)
        # LED滚动显示的计时器
        self.timer_LED = QtCore.QTimer(self)
        # LED显示顺序的下标
        self.led_subscript = 0
        # 利用此定时器每隔一段时间自动刷新下拉列表
        self.timer_refresh = QtCore.QTimer(self)
        # 控件初始化&建立connect函数
        self.create_window()

    def create_window(self):
        self.resize(resolution_x, resolution_y)
        self.setWindowTitle("控制中心")

        self.name_label.setGeometry(gl*31, gly*7, gl*6, gly*1)
        self.name_label.setText("请选择人员:")

        self.comboBox.setGeometry(QtCore.QRect(gl * 30, gly*9, gl*9, gly*2))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.clear()
        self.comboBox.addItem('请选择')
        self.comboBox.currentIndexChanged.connect(self.combo_index_changed)

        self.work_label.setGeometry(gl * 5, gly*10, gl*20, gly*15)

        self.print_button.setGeometry(gl * 30, gly * 17, gl * 9, gly * 4)
        self.print_button.setText("打印")
        self.print_button.clicked.connect(self.print_clicked)

        self.combo_refresh_button.setGeometry(gl * 30, gly * 2, gl * 9, gly * 4)
        self.combo_refresh_button.setText("刷新")
        self.combo_refresh_button.clicked.connect(self.combo_list_refresh)

        self.timer_LED.start(5000)
        self.timer_LED.timeout.connect(self.led_refresh)

        self.timer_refresh.start(30000)
        self.timer_refresh.timeout.connect(self.combo_list_refresh)

        self.show()

    # 下拉列表选项改变的槽函数
    def combo_index_changed(self):
        self.work_label.setText(self.comboBox.currentData())

    # 刷新下拉列表的槽函数
    def combo_list_refresh(self):
        print("combo_refresh")
        self.data_copy = data.data
        self.comboBox.clear()
        for k, v in data.data.items():
            self.comboBox.addItem(k, v)

    # 刷新LED显示内容的槽函数
    def led_refresh(self):
        if self.led_subscript > len(self.data_copy) - 1:
            self.led_subscript = 0
        # 此函数将字符串显示在LED上
        # LEDProjecting.LEDShow()
        self.led_subscript += 1

    # 打印的槽函数
    def print_clicked(self):
        print(self.comboBox.currentText()+':'+self.comboBox.currentData())
        # 此函数用于打印内容
        # serialPrinting.sprint(self.comboBox.currentText()+':'+self.comboBox.currentData())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
