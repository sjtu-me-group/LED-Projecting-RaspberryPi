# LED-Projecting-RaspberryPi

##运行环境##Linux kernel 4.x\n
项目语言为Python3，使用的库为:
  +sys
  +socket
  +PyQt5
  +...  
项目包含5个Python文件，分别为：
  +main.py
  +socket.py
  +data.py
  +LEDProjecting.py
  +serialPring.py
GUI进程与网络进程通过data.py中的字典沟通。网络进程每10s从服务器下载一次data.py；主进程每30s读取一次data.py。
