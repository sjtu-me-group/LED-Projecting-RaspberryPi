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


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # 显示时间
        self.time_label = QtWidgets.QLabel(self)
        self.timer_time = QtCore.QTimer(self)
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
        self.state_label = QtWidgets.QLabel(self)
        # 按下此按钮刷新人员下拉列表
        self.combo_refresh_button = QtWidgets.QPushButton(self)
        # LED滚动显示的计时器
        self.timer_LED = QtCore.QTimer(self)
        # LED显示顺序的下标
        self.led_subscript = 0
        # 利用此定时器每隔一段时间自动刷新下拉列表
        self.timer_refresh = QtCore.QTimer(self)
        # 退出按钮
        self.quit_button = QtWidgets.QPushButton(self)
        # 控件初始化&建立connect函数
        self.create_window()

    def create_window(self):
        self.resize(resolution_x, resolution_y)
        self.setWindowTitle("控制中心")

        self.timer_time.start(1000)
        self.time_label.setGeometry(gl*2, gl*1, gl*3, gl*2)
        self.timer_time.timeout.connect(self.time_refresh)

        self.name_label.setGeometry(gl*30, gl*8, gl*6, gl*1)
        self.name_label.setText("请选择人员:")

        self.comboBox.setGeometry(QtCore.QRect(gl * 30, gl*9, gl*9, gl*2))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.clear()
        self.comboBox.addItem('请选择')
        self.comboBox.currentIndexChanged.connect(self.combo_index_changed)

        self.work_label.setGeometry(gl * 2, gl*5, gl*20, gl*15)

        self.print_button.setGeometry(gl * 30, gl * 14, gl * 9, gl * 4)
        self.print_button.setText("打印")
        self.print_button.clicked.connect(self.print_clicked)

        self.state_label.setGeometry(gl * 2, gl * 22, gl * 4, gl * 1)

        self.combo_refresh_button.setGeometry(gl * 30, gl * 2, gl * 9, gl * 4)
        self.combo_refresh_button.setText("刷新")
        self.combo_refresh_button.clicked.connect(self.combo_list_refresh)

        self.timer_LED.start(5000)
        self.timer_LED.timeout.connect(self.led_refresh)

        self.timer_refresh.start(30000)
        self.timer_refresh.timeout.connect(self.combo_list_refresh)

        self.quit_button.setGeometry(gl * 30, gl * 19, gl * 9, gl * 4)
        self.quit_button.setText("退出程序")
        self.quit_button.clicked.connect(self.closeEvent)

        self.show()

    # 显示时间的槽函数
    def time_refresh(self):
        second1 = QtCore.QTime.currentTime().second()
        minute1 = QtCore.QTime.currentTime().minute()
        hour1 = QtCore.QTime.currentTime().hour()
        # 在小于10的数字前加0
        h1 = ''
        m1 = ''
        s1 = ''
        if hour1 < 10:
            h1 = '0'
        if minute1 < 10:
            m1 = '0'
        if second1 < 10:
            s1 = '0'
        self.time_label.setText("当前时间" + '\n' + h1 + str(hour1) + ':' + m1 + str(minute1) + ':' + s1 + str(second1))

    # 下拉列表选项改变的槽函数
    def combo_index_changed(self):
        self.work_label.setText(self.comboBox.currentText() + "的工作是：" + '\n' + str(self.comboBox.currentData()))

    # 刷新下拉列表的槽函数
    def combo_list_refresh(self):
        print("combo_refresh")
        try:
            self.data_copy = data.data
        except:
            self.state_label.setText("没有数据！")
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
        try:
            print(self.comboBox.currentText() + "的工作是：" + '\n' + str(self.comboBox.currentData()))
            self.state_label.setText("打印成功！")
        except:
            self.state_label.setText("没有数据！")
        # 此函数用于打印内容
        # serialPrinting.sprint(self.comboBox.currentText()+':'+self.comboBox.currentData())

    def closeEvent(self, QCloseEvent):
        #  使用QMessageBox提示
        reply = QtWidgets.QMessageBox.warning(self, "退出程序", "即将退出, 确定？", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            QCloseEvent.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showFullScreen()
    sys.exit(app.exec_())
