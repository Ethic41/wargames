#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-08 04:09:27
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from pwn import *
from PIL import Image

def main():
    flag_image = Image.open("flag.png")
    lemur_image = Image.open("lemur.png")

    flag_image_bytes = flag_image.tobytes()
    lemur_image_bytes = lemur_image.tobytes()
    result_bytes = xor(lemur_image_bytes, flag_image_bytes)

    result_image = lemur_image.copy()
    result_image.frombytes(result_bytes)

    result_image.save("result.png")
    print("done :).")


if __name__ == "__main__":
    main()

