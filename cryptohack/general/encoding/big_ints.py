#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-02 18:25:49
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from Crypto.Util.number import long_to_bytes

def main():
    long_num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    print(long_to_bytes(long_num))


if __name__ == "__main__":
    main()

