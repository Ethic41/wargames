#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-07 18:01:31
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

from pwn import *

context.arch = "i386"

# filename = ""
# binary_target = ELF(filename)
# target_process = process(filename)


def exploit():
    pass


def solution():
    assembly = """
    my_entry:
        push 0xd3c8b139
        push 0xd48672ae
        push 0xd73346ed
        call asm3
    asm3:
        push   ebp
        mov    ebp,esp
        xor    eax,eax
        mov    ah,BYTE PTR [ebp+0xa] 
        shl    ax,0x10
	    sub    al,BYTE PTR [ebp+0xc]
	    add    ah,BYTE PTR [ebp+0xd]
	    xor    ax,WORD PTR [ebp+0x10]
	    nop
	    pop    ebp
	    ret    
    """
    
    my_elf = ELF.from_assembly(assembly, vma=0x400000)
    my_elf.save("asm3")


def debug():
    pass


if __name__ == "__main__":
    # debug()
    exploit()


