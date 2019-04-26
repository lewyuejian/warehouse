#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: tcp_socket.py
@time: 2019/4/26 11:09
@desc:
'''
import socket
def main(data):
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    udp_socket.connect(('39.108.197.42', 7788))
    udp_socket.send(bytes().fromhex(data))
    udp_socket.close()

if __name__ == '__main__':
    hus = '7E0200002201365645451200010000000000040002015193BA06CF3BDA00000000000019042611083301040000092E367E'
    main(hus)