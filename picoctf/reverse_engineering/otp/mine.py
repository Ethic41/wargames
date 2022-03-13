#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-03-09 11:12:44
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


import gdb # type: ignore


def exploit():
    pass


def solution():
    pass


counter = 0

def solve():
    look_up_keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    found_keys = []
    jumbled = "lfmhjmnahapkechbanheabbfjladhbplbnfaijdajpnljecghmoafbljlaamhpaheonlmnpmaddhngbgbhobgnofjgeaomadbidl"

    gdb.execute("start")
    gdb.execute("break *main+208")
    gdb.execute("break *main+291")
    
    def get_frame_register_value(register_name):
        frame = gdb.selected_frame()
        register = frame.read_register(register_name)
        return register.format_string()
    
    def get_frame_register_value_as_int(register_name):
        value = get_frame_register_value(register_name)
        return int(value, 16)
    
    def run(arg):
        if counter > 0:
            gdb.execute(f"ignore 1 {counter}")
            gdb.execute(f"ignore 2 {counter - 1}")
        gdb.execute(f"run {arg}")
        return get_frame_register_value_as_int("rdx")


    def compute_key(key: int):
        return 0x61 + key
    

    def look_up_key(jumbled_value: str):
        if counter == 0:
            for current_key in look_up_keys:
                if ord(jumbled_value) == compute_key(run(current_key)):
                    return current_key
        else:
            past_keys = "".join(found_keys)
            for current_key in look_up_keys:
                if ord(jumbled_value) == compute_key(run(past_keys + current_key)):
                    return current_key


    def brute_force_key():
        global counter
        for jum_val in jumbled:
            valid_key = look_up_key(jum_val)
            found_keys.append(valid_key)
            print(f"key for {counter} iteration: {valid_key}")
            counter += 1
        print("".join(found_keys))
    
    brute_force_key()


def debug():
    pass


if __name__ == "__main__":
    # debug()
    # exploit()
    solve()

