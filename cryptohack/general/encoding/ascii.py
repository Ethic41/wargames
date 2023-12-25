#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-02 17:30:59
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def main():
    int_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    flag = ""

    for integer in int_list:
        flag += chr(integer)
    
    print(flag)


if __name__ == "__main__":
    main()

