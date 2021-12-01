#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-11-28 08:22:26
# @Author  : Dahir Muhammad Dahir
# @Description : something cool

from typing import Dict, List, Tuple
import os
from time import sleep

MAZE_WIDTH = 28
MAZE_HEIGHT = 12
MAZE: List[List[str]] = []


def initialize_maze():
    for i in range(MAZE_HEIGHT):
        MAZE.append(['=' for j in range(MAZE_WIDTH)])
    MAZE[0][0] = 'o'
    MAZE[-1][-1] = '#'


def get_random_number(seed):
    prod = seed * 0x41c64e6d
    bin_prod = bin(prod)[2:]
    difference = 32 - (64 - len(bin_prod))
    return int(bin_prod[difference:], 2) + 12345


def fill_maze(seed):
    rand_num = seed
    for i in range(MAZE_WIDTH):
        rand_num = get_random_number(rand_num)
        for j in range(MAZE_HEIGHT):
            rand_num = get_random_number(rand_num)
            if MAZE[j][i] == 'o' or MAZE[j][i] == '#':
                continue
            if rand_num & 0x51 == 0x51:
                MAZE[j][i] = 'X'
            else:
                MAZE[j][i] = ' '



def print_maze():
    print(f"+{MAZE_WIDTH * '-'}+")

    for maze_line in MAZE:
        print(f"|{''.join(maze_line)}|")
    
    print(f"+{MAZE_WIDTH * '-'}+")


def solve_mine():
    x = 0
    y = 0
    count = 0
    string_out = ""
    while True:
        print_maze()
        #sleep(0.8)
        clean_screen()
        if MAZE[x][y] == "#":
            print_maze()
            break

        if is_path(x, y):
            visit_path(x, y)
        
        prev_x, prev_y = x, y
        x, y = get_next_path(x, y)

        string_out += get_direction(prev_y, prev_x, y, x)
        if x == 0 and y == 0:
            string_out = ""
        count += 1
    print(f"Maze Solved in {count} steps")
    print(f"Path taken: {string_out}")


def get_direction(prev_x, prev_y, x, y):
    if x > prev_x:
        return "r"
    if x < prev_x:
        return "l"
    if y > prev_y:
        return "d"
    if y < prev_y:
        return "u"


def is_path(x, y):
    if x > MAZE_HEIGHT - 1 or y > MAZE_WIDTH - 1:
        return False 
    
    if x < 0 or y < 0:
        return False
    
    if MAZE[x][y] == "X":
        return False
    
    return True


def visit_path(x, y):
    path = MAZE[x][y]
    if path == ' ':
        MAZE[x][y] = "1"
    elif path == 'o':
        MAZE[x][y] = "1"
    elif path and path != "#":
        MAZE[x][y] = f"{int(path)+1}"


def get_next_path(x, y):
    possible_path = []
    if is_path(x+1, y):
        possible_path.append((x+1, y))
    
    if is_path(x-1, y):
        possible_path.append((x-1, y))
    
    if is_path(x, y+1):
        possible_path.append((x, y+1))
    
    if is_path(x, y-1):
        possible_path.append((x, y-1))
    
    return choose_best_path(possible_path)


def choose_best_path(possible_path: List[Tuple]):
    paths: Dict = {}
    for path in possible_path:
        if MAZE[path[0]][path[1]] == '#':
            return path
        if MAZE[path[0]][path[1]] == ' ':
            path_weight = 0
            if path_weight in paths:
                path = analyse_best_path(paths[path_weight], path)
            paths[path_weight] = path
            continue
        path_weight = int(MAZE[path[0]][path[1]])
        if path_weight in paths:
            path = analyse_best_path(paths[path_weight], path)
        paths[path_weight] = path
    
    return paths[min(paths.keys())]


def analyse_best_path(new_path, existing_path):
    existing_path_x, existing_path_y = existing_path
    new_path_x, new_path_y = new_path
    if existing_path_x == new_path_x:
        if new_path_y > existing_path_y:
            return new_path
        else:
            return existing_path
    if existing_path_y == new_path_y:
        if new_path_x > existing_path_x:
            return new_path
        else:
            return existing_path
    
    if existing_path_x > new_path_x:
        return existing_path
    else:
        return new_path


def clean_screen():
    os.system("clear")

def main():
    seed = 1638208411
    initialize_maze()
    fill_maze(seed)
    print_maze()
    solve_mine()


if __name__ == '__main__':
    main()

