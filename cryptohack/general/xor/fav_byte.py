#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-03 04:18:21
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from pwn import *


def main():
    cipher = unhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

    for i in range(1, 257):
        print(f"current i: {i}")
        candidate = xor(cipher, chr(i).encode()).decode()

        if "crypto" in candidate:
            print(candidate)
            break


if __name__ == "__main__":
    main()

