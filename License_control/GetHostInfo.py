# -*- coding: UTF-8 -*-
# 获取计算机的物理地址

import socket
import struct
import fcntl
import uuid

def getHwAddr():
    """
    获取主机物理地址
    """
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
    

if __name__ == '__main__':
    print(getHwAddr())

