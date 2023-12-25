#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-08-05 16:44:31
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *
from pwn import p32

context.arch = "i386"

filename = "./babystack"
binary_target = ELF(filename)
target_process = process(filename)


def exploit():
    pass


def solve():
    pass


def debug():
    script = """
    break *0x804846d
    break *0x804844a
    break *0x8048451
    """
    
    gdb.attach(target_process, gdbscript=script)

    pause()
    pause()

    trash = cyclic(0x50)
    target_process.send(trash)

    target_process.interactive()


if __name__ == "__main__":
    # debug()
    exploit()
    # solve()


