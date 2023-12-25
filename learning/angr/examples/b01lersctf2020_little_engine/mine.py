#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-14 10:35:27
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


# from pwn import *
from angr.sim_state import SimState
import angr
import claripy

# context.arch = "i386"

# filename = ""
# binary_target = ELF(filename)
# target_process = process(filename)


def exploit():
    pass


def solve():
    base_address = 0x400000
    project = angr.Project("./engine", auto_load_libs=True, main_opts={'base_addr': base_address})
    
    flag_chars = []
    input_len = 1+75*4
    for i in range(input_len):
        flag_chars.append(claripy.BVS(f"x_{i}", 8))
    
    target_input = claripy.Concat(*flag_chars + [claripy.BVV(b'\n')])

    state: SimState = project.factory.full_init_state(args=["./engine"], \
        add_options=angr.options.unicorn, stdin=target_input)
    
    for flag_char in flag_chars:
        state.solver.add(flag_char < 0x7f)
        state.solver.add(flag_char > 0x20)
    
    sim_mgr = project.factory.simgr(state)
    sim_mgr.run()

    win_state = []
    for fin_state in sim_mgr.deadended:
        if b"Chugga" in fin_state.posix.dumps(1):
            win_state.append(fin_state)
    
    valid_state = win_state[0].posix.dumps(0)
    valid_chars = [ chr(valid_state[i]) for i in range(0, len(valid_state), 2)]
    flag = "".join(valid_chars)[1:76]
    print(flag)


def debug():
    pass


if __name__ == "__main__":
    # debug()
    # exploit()
    solve()

