#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-08 00:22:41
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
    mine:
        push 0x2d
        push 0x4
        call asm2
    asm2:
	    push   ebp
	    mov    ebp,esp
	    sub    esp,0x10
	    mov    eax,DWORD PTR [ebp+0xc]
	    mov    DWORD PTR [ebp-0x4],eax
	    mov    eax,DWORD PTR [ebp+0x8]
	    mov    DWORD PTR [ebp-0x8],eax
	    jmp    asm2+31
	    add    DWORD PTR [ebp-0x4],0x1
	    add    DWORD PTR [ebp-0x8],0xd1
	    cmp    DWORD PTR [ebp-0x8],0x5fa1
	    jle    asm2+20
	    mov    eax,DWORD PTR [ebp-0x4]
	    leave  
	    ret    
    """

    my_elf = ELF.from_assembly(assembly, vma=0x400000)
    my_elf.save("asm2")


def debug():
    pass


if __name__ == "__main__":
    # debug()
    exploit()


