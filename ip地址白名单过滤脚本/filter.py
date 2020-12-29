# -*- coding:utf-8 -*-
# @Time : 2020/9/11 10:37 
# @Author : alee
# @File : main.py 
# @Software: PyCharm
# purpose: ip地址去重操作，去重包含c段，和伪b段，以及部分单ip

from IPy import IP

def readSourceFile():
    ip_source_f = open('source.txt', 'r')
    return ip_source_f

def readWhiteFile():
    ip_white_f = open('whitelist.txt', 'r')
    return ip_white_f

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

def writeFile(wnum,snum):
    wf = open('inwhitenumber.txt','w')
    df = open('dealnumber.txt','w')
    if( len(wnum) != 0):
        print('正在向inwhitenumber.txt中写入白名单ip条目……')
        for x in wnum:
            wf.write(str(x) + '\n')
        wf.close()
        print('写入完成！')
    print('开始向dealnumber.txt中写入需要处置的ip条目……')
    for y in snum:
        df.write(str(y) + '\n')
    df.close()
    print('写入完成！')

if __name__ == '__main__':
    sourcef = readSourceFile()
    whitef = readWhiteFile()
    sourceline = getLineIP(sourcef)
    sourcelist = set(getListIP(sourceline))
    whiteline = getLineIP(whitef)
    whitelist = set(getListIP(whiteline))
    # 交集，得出不能封堵的单个ip地址
    whitenum = sourcelist & whitelist
    # 将这个部分转换成c段地址
    white_d = set()
    for i in whitenum:
        white_d.add(str(i))
    white_c = set(ipToC(whitenum))
    dealline = set(sourceline)
    deallist1 = dealline - white_d
    deallist2 = deallist1 - white_c
    writeFile(whitenum,deallist2)
    # input('Press Any Key')
