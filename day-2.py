'''Day 2: Rock paper scissor

https://adventofcode.com/2022/day/2'''

# part 1

from toolkit import *
## A: rock, B: paper, C: scissor
## X: Rock, Y: Paper, Z: Scissor

## points: Rock, X:1, Paper, Y: 2, Scissor, Z: 3

inp_test = inputfile('input_files/test_files/day-2.txt')
inp_day2 = inputfile('input_files/day-2.txt')

win_list = ['A Y', 'B Z', 'C X']
draw_list = ['A X', 'B Y', 'C Z']

def calculate_score(input_f):
    """"""
    wins = sum([6 for x in input_f if x in win_list])
    draws = sum([3 for x in input_f if x in draw_list])
    rock = sum ([1 for x in input_f if x[-1] == 'X'])
    paper = sum ([2 for x in input_f if x[-1] == 'Y'])
    scissor = sum ([3 for x in input_f if x[-1] == 'Z'])
    score = wins + draws + rock + paper + scissor
    return score

assert calculate_score(inp_test) == 15

print(calculate_score(inp_day2))




