#!/usr/bin/python
#coding=utf-8
import socket
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print('%d端口开放' % tgtPort)
        connSkt.close()
    except:
	    print('%d端口关闭' % tgtPort)
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("无法解析的主机名" % tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n扫描的主机IP地址是: ' + tgtName[0])
    except:
        print('\n扫描的主机IP地址是: ' + tgtIP)
        socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('正在扫描的端口：' + str(tgtPort))
        connScan(tgtHost, int(tgtPort))

a=raw_input("请输入要检测的目标主机:")
b=input("是否扫描默认端口?是请输入1，需要自定义端口请输入2:")
if(b==2):
    c=input("请输入需要扫描的端口，用[]括起来：")
    print("正在扫描自定义端口...")
    portScan(a,c)
else:
    print("正在扫描默认端口...")
    portScan(a, [80,443,3389,1433,23,445])
