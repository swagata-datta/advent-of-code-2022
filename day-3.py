"""Day 3 - advent of code 2022:
Rucksack compartments

https://adventofcode.com/2022/day/3"""

# part 1

from toolkit import *
import string

inp_test = inputfile('input_files/test_files/day-3.txt')
inp_day3 = inputfile('input_files/day-3.txt')

def get_duplicates(input_f):
    '''Get's a list of duplicate items given the input'''
    duplicates = []
    for rucksack in input_f:
        length = len(rucksack) // 2                     # gets the length of the rucksack
        rucksack1 = rucksack[:length]                   # first compartment
        rucksack2 = rucksack[length:]                   # second compartment
        inters = set(rucksack1).intersection(rucksack2) # finds the intersection
        duplicates += list(inters)

    return duplicates  


def get_part1(dup):
    """Gets the sum of priority, given the duplicate list"""
    alph = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    num = list(range(1,53))
    priority = dict(zip(alph, num))
    score = sum([priority[x] for x in dup])

    return score

assert get_part1(get_duplicates(inp_test)) == 157

#print('Part 1: ', get_part1(get_duplicates(inp_day3)))

# part 2

def get_part2(input_f):
    """finds the intersection of three rucksacks"""
    new_inp = [input_f[i: i+3] for i in range(0, len(input_f), 3)] # separates input in three rucksacks
    badges = []
    for x in new_inp:
        badges += set(x[0]).intersection(x[1]).intersection(x[2])

    alph = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    num = list(range(1,53))
    priority = dict(zip(alph, num))
    score = sum([priority[x] for x in badges])

    return score

assert get_part2(inp_test) == 70
print('Part 2: ', get_part2(inp_day3))

