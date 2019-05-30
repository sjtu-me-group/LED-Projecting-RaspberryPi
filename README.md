# LED-Projecting-RaspberryPi

## 运行环境
Linux kernel 4.x
## 库
  + sys
  + socket
  + PyQt5
  + ...  
## 文件
  + main.py
  + socket.py
  + data.py
  + LEDProjecting.py
  + serialPring.py
## 通信方式
GUI进程与网络进程通过data.py中的字典沟通。网络进程每10s从服务器下载一次data.py；主进程每30s读取一次data.py。
