#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-03 05:21:43
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from pwn import *


def main():
    cipher = unhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
    target = "crypto"

    begin = 0
    end = len(target)

    for i in range(int(len(cipher) / len(target))):
        print(xor(target, cipher[begin:end]))

        begin = end
        end += len(target)


if __name__ == "__main__":
    main()

