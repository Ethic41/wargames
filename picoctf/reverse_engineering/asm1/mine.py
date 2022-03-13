#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-07 23:31:58
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
        push 0x2e0
        call asm1
    asm1:
        push   ebp
        mov    ebp,esp
        cmp    DWORD PTR [ebp+0x8],0x3fb
	    jg     asm1+37
	    cmp    DWORD PTR [ebp+0x8],0x280
	    jne    asm1+29
	    mov    eax,DWORD PTR [ebp+0x8]
	    add    eax,0xa
	    jmp    asm1+60
	    mov    eax,DWORD PTR [ebp+0x8]
	    sub    eax,0xa
	    jmp    asm1+60
	    cmp    DWORD PTR [ebp+0x8],0x559
	    jne    asm1+54
	    mov    eax,DWORD PTR [ebp+0x8]
	    sub    eax,0xa
	    jmp    asm1+60
	    mov    eax,DWORD PTR [ebp+0x8]
	    add    eax,0xa
	    pop    ebp
	    ret    
    """

    my_elf = ELF.from_assembly(assembly, vma=0x400000)
    my_elf.save("asm1")


def debug():
    pass


if __name__ == "__main__":
    # debug()
    exploit()


