import sys
import os

if __name__ == '__main__':
  def sprint(input):
    os.system('sudo chmod a+w /dev/usb/lp0')
    shellPast = "sudo echo -e " + repr(str(input))+ "> /dev/usb/lp0"
    os.system(shellPast)
