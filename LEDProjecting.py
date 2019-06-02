import sys
import serial

s = serial.Serial("/dev/ttyS0", 57600)
s.close()

def LEDshow(ostr): 
    
    def sub(string,p,c):
        new = []
        for s in string:
            new.append(s)
        new[p] = c
        return ''.join(new)
    
    nstr=b''
    for ch in ostr:
        ch1=ch.encode("gb2312")
        if b'\xa1\xa0'<=ch1<=b'\xf7\xff':
            nstr=nstr+ch1
        else:
            nstr=nstr+ch.encode("ascii")
    #print(nstr)
    l=len(nstr)
    l=hex(l)
    l=sub(l,0,'x')
    l=l.strip('x')
    if len(l)==1:
        l="0"+l
    nstr=bytes.fromhex(l)+b'\x00\x00\x00'+nstr
    nstr=b'\x00\x00\x00\x00\x00\x08\x00\x20\x00\x00\x00\x00\x01\x00\x00\x00\x00\x02\x02\x01\x00\x10\x0A'+nstr
    #print(nstr)
    l=len(nstr)
    l=hex(l)
    l=sub(l,0,'x')
    l=l.strip('x')
    if len(l)==1:
        l="0"+l
    nstr=bytes.fromhex(l)+b'\x00'+nstr
    nstr=b'\xA3\x06\x01\x34\x00\x00\x01'+nstr
    l=len(nstr)
    l=hex(l)
    print(l)
    l=sub(l,0,'x')
    #print(l)
    l=l.strip('x')
    #print(l)
    if len(l)==1:
        l="0"+l
    nstr=bytes.fromhex(l)+b'\x00'+nstr
    nstr=b'\x01\x00\x00\x80\x00\x00\x00\x00\x00\x00\xFE\x02'+nstr
    #print(nstr)
    
    lenth=len(nstr)
    P=0xa001
    crc=0x0
    for i in range(0,lenth):
        crc=nstr[i]^crc
        for j in range(0,8):
            if((crc&0x1)==1):
                crc=(crc>>1)^P
            else:
                crc>>=1
    #print(crc)
    crc=hex(crc)
    crc=sub(crc,0,'x')
    crc=crc.strip('x')
    if len(crc)==3:
        crc="0"+crc
    else:
        if len(crc)==2:
            crc="00"+crc
    c1=crc[2:4]
    c2=crc[0:2]
    #print(c1)
    #print(c2)
    nstr=b'\xa5\xa5\xa5\xa5\xa5\xa5\xa5\xa5'+nstr+bytes.fromhex(c1)+bytes.fromhex(c2)+b'\x5a'
    #print(nstr)
    s.open()
    s.write(nstr)
    s.close()
    return nstr

LEDshow("机电系统")
