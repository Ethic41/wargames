#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-09 22:22:29
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def main():
    print(gcd(252, 105))


def naive_gcd(a, b):
    while True:
        print(f"current: a => {a}  b => {b}")
        if a == b:
            return a
        
        if a > b:
            a -= b
        else:
            b -= a


def gcd(a, b):
    while True:
        if a == 0:
            return b
        if b == 0:
            return a
        if a > b:
            a %= b
        else:
            b %= a


if __name__ == "__main__":
    main()

