#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-02 23:15:59
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def main():
    test_input = "label"
    target_num = 13
    new_string = ""

    for i in test_input:
        new_string += chr(ord(i) ^ target_num)
        print("time")
    
    print(f"crypto{{{new_string}}}")


if __name__ == "__main__":
    main()

