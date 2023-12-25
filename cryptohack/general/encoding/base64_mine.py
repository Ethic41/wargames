#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-02 17:49:03
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


import binascii
import base64

def main():
    input_str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    print(base64.b64encode(binascii.unhexlify(input_str)))


if __name__ == "__main__":
    main()

