'''
Day 6: Communication system

https://adventofcode.com/2022/day/6'''

# test input has 5 different strings

from toolkit import *

inp_test = inputfile('input_files/test_files/day-6.txt')    # this is a list. Every element a separate string
inp_day6 = inputfile('input_files/day-6.txt', lines=False)

def part1(inp):
    """Takes a string. Returns the number of letter it needs to process
    before getting four consecutive distinct letters"""
    # I will use the fact that a set cannot have duplicates
    count = 4
    for i in range(len(inp)-3):
        if len(set(inp[i:i+4])) == 4:
            return count
        else:
            count += 1

assert part1(inp_test[0]) == 7
assert part1(inp_test[1]) == 5
assert part1(inp_test[2]) == 6
assert part1(inp_test[3]) == 10
assert part1(inp_test[4]) == 11

print('Part 1: ', part1(inp_day6))

def part2(inp):
    """Takes a string. Returns the number of letter it needs to process
    before getting 14 consecutive distinct letters"""
    # I will use the fact that a set cannot have duplicates
    count = 14
    for i in range(len(inp)-13):
        if len(set(inp[i:i+14])) == 14:
            return count
        else:
            count += 1

assert part2(inp_test[0]) == 19
assert part2(inp_test[1]) == 23
assert part2(inp_test[2]) == 23
assert part2(inp_test[3]) == 29
assert part2(inp_test[4]) == 26

print('Part 2: ', part2(inp_day6))