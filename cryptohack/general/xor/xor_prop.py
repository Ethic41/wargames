#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-02 23:37:19
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from binascii import unhexlify


def main():
    KEY1 = unhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
    KEY2_KEY1 = unhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
    KEY2_KEY3 = unhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
    KEYED_FLAG = unhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

    flag = xor(KEYED_FLAG, KEY2_KEY3, KEY1)
    print(flag)


def get_int_key(str_key):
    return bytes_to_long(unhex(str_key))


def hex_str_key(int_key):
    return hex(int_key)[2:]


if __name__ == "__main__":
    main()

