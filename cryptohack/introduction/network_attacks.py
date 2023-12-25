#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-02 17:14:55
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from pwn import *
from json import dumps as json_encode
from json import loads as json_decode


def main():
    connection = remote("socket.cryptohack.org", 11112)
    print(connection.recvline())
    print(connection.recvline())
    print(connection.recvline())
    print(connection.recvline())

    req = json_encode({"buy": "flag"}).encode()

    connection.send(req)

    print(connection.recvline())


if __name__ == "__main__":
    main()
