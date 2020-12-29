# -*- coding:utf-8 -*-
# @Time : 2020/9/11 10:37
# @Author : alee
# @File : main.py
# @Software: PyCharm
# purpose: ip地址去重操作，去重包含c段，和伪b段，以及部分单ip

from IPy import IP

def readSourceFile():
    ip_source_f = open('iplist.txt', 'r')
    return ip_source_f


def getLineIP(ipf):
    ipLine = []
    texts = ipf.readlines()
    texts = set(texts)
    for text in texts:
        ip = text.strip()
        ipLine.append(ip)
    return ipLine

def getListIP(ipLine):
    ipList = []
    for line in ipLine:
        ip = IP(line)
        for x in ip:
            ipList.append(x)
    return ipList

def ipToC(list):
    ips = set()
    retip = []
    for ip in list:
        ipc = IP(ip).make_net('255.255.255.0')
        if ipc not in ips:
            ips.add(ipc)
            retip.append(str(ipc))
    return retip

def writeFile(wnum):
    wf = open('IPC.txt','w')
    if( len(wnum) != 0):
        print('正在向inwhitenumber.txt中写入白名单ip条目……')
        for x in wnum:
            wf.write(str(x) + '\n')
        wf.close()
        print('写入完成！')

if __name__ == '__main__':
    sourcef = readSourceFile()
    sourceline = getLineIP(sourcef)
    sourcelist = set(getListIP(sourceline))
    # 将这个部分转换成c段地址
    white_d = set()
    for i in sourcelist:
        white_d.add(str(i))
    ipc = set(ipToC(sourcelist))
    writeFile(ipc)
