#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-08 00:41:41
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
        push ebp
        mov ebp, esp
        sub esp, 0x10
        mov DWORD PTR [ebp-0x10], 0x6f636970
        mov DWORD PTR [ebp-0xC], 0x5f465443
        mov DWORD PTR [ebp-0x8], 0x31313361
        mov DWORD PTR [ebp-0x4], 0x32
        lea eax, [ebp-0x10]
        push eax
        call asm4
    asm4:
	    push   ebp
	    mov    ebp,esp
	    push   ebx
	    sub    esp,0x10
	    mov    DWORD PTR [ebp-0x10],0x246
	    mov    DWORD PTR [ebp-0xc],0x0
	    jmp    asm4+27
	    add    DWORD PTR [ebp-0xc],0x1
	    mov    edx,DWORD PTR [ebp-0xc]
	    mov    eax,DWORD PTR [ebp+0x8]
	    add    eax,edx
	    movzx  eax,BYTE PTR [eax]
	    test   al,al
	    jne    asm4+23
	    mov    DWORD PTR [ebp-0x8],0x1
	    jmp    asm4+138
	    mov    edx,DWORD PTR [ebp-0x8]
	    mov    eax,DWORD PTR [ebp+0x8]
	    add    eax,edx
	    movzx  eax,BYTE PTR [eax]
	    movsx  edx,al
	    mov    eax,DWORD PTR [ebp-0x8]
	    lea    ecx,[eax-0x1]
	    mov    eax,DWORD PTR [ebp+0x8]
	    add    eax,ecx
	    movzx  eax,BYTE PTR [eax]
	    movsx  eax,al
	    sub    edx,eax
	    mov    eax,edx
	    mov    edx,eax
	    mov    eax,DWORD PTR [ebp-0x10]
	    lea    ebx,[edx+eax*1]
	    mov    eax,DWORD PTR [ebp-0x8]
	    lea    edx,[eax+0x1]
	    mov    eax,DWORD PTR [ebp+0x8]
	    add    eax,edx
	    movzx  eax,BYTE PTR [eax]
	    movsx  edx,al
	    mov    ecx,DWORD PTR [ebp-0x8]
	    mov    eax,DWORD PTR [ebp+0x8]
	    add    eax,ecx
	    movzx  eax,BYTE PTR [eax]
	    movsx  eax,al
	    sub    edx,eax
	    mov    eax,edx
	    add    eax,ebx
	    mov    DWORD PTR [ebp-0x10],eax
	    add    DWORD PTR [ebp-0x8],0x1
	    mov    eax,DWORD PTR [ebp-0xc]
	    sub    eax,0x1
	    cmp    DWORD PTR [ebp-0x8],eax
	    jl     asm4+51
	    mov    eax,DWORD PTR [ebp-0x10]
	    add    esp,0x10
	    pop    ebx
	    pop    ebp
	    ret    
    """
    my_elf = ELF.from_assembly(assembly, vma=0x400000)
    my_elf.save("asm4")


def debug():
    pass


if __name__ == "__main__":
    # debug()
    exploit()


