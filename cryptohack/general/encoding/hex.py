#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-02 17:44:43
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


import binascii

def main():
    input_hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
    print(binascii.unhexlify(input_hex).decode())


if __name__ == "__main__":
    main()

