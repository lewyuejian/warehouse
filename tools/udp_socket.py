#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: udp_socket.py
@time: 2019/4/26 10:28
@desc:
'''
import socket
def main(data,IP):
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.sendto(data,(IP,6688))
    udp_socket.close()

if __name__ == '__main__':

    hus = "2929800028C13D990B190425165122022320041140156000000000F80000007E7C0000001E0000000000005E0D"
    data = bytes().fromhex(hus)
    main(data,'120.0.0.1')
