#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import codecs

sys.stdout = codecs.getwriter("utf8")(sys.stdout)
sys.stderr = codecs.getwriter("utf8")(sys.stderr)

def nb(grid, x, y):
    ret = 0
    if x > 0 and y > 0 and grid[x-1][y-1]: ret += 1
    if x > 0 and grid[x-1][y]: ret += 1
    if y > 0 and grid[x][y-1]: ret += 1

    if x < 99 and y < 99 and grid[x+1][y+1]: ret += 1
    if x < 99 and grid[x+1][y]: ret += 1
    if y < 99 and grid[x][y+1]: ret += 1

    if x < 99 and y > 0 and grid[x+1][y-1]: ret += 1
    if x > 0 and y < 99 and grid[x-1][y+1]: ret += 1

    return ret

def corner(x, y): return (x,y) in [(0,0),(0,99),(99,0),(99,99)]

if __name__ == "__main__":
    grid = [[False for i in xrange(100)] for i in xrange(100)]
    with codecs.open("input", "r", "utf-8") as f:
        for x,line in enumerate(f):
            line = line.strip()
            if not line: continue

            for y,c in enumerate(line):
                if c == "#": grid[x][y] = True

    for step in xrange(100):
        grid_nxt = [[False for i in xrange(100)] for i in xrange(100)]

        for x in xrange(100):
            for y in xrange(100):

                n = nb(grid, x, y)
                if grid[x][y] and n in [2,3]:
                    grid_nxt[x][y] = True
                elif not grid[x][y] and n == 3:
                    grid_nxt[x][y] = True
        grid = grid_nxt

    ans = 0
    for x in xrange(100):
        for y in xrange(100):
            if grid[x][y]: ans += 1
    print ans
