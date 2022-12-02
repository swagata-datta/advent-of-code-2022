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

#print('Part 1:', calculate_score(inp_day2))

## part 2


def calculate_part2(input_f):
    """Calculates"""
    # creating three lists for win, draw, and loss
    win_list = [x[0] for x in input_f if x[-1] == 'Z']
    draw_list = [x[0] for x in input_f if x[-1] == 'Y']
    loss_list = [x[0] for x in input_f if x[-1] == 'X']

    # for wins, if opponent plays rock, I play paper and get 2 points, paper implies 3 points and so on
    win_dic = {'A': 2, 'B':3, 'C':1}
    win_shape = [win_dic[x] for x in win_list] # list of points for the wins
    draw_dic = {'A': 1, 'B':2, 'C':3}
    draw_shape = [draw_dic[x] for x in draw_list]
    # for loss, if opponet plays rock, I play scissor and get 3 points, paper implies 1 points and so on
    loss_dic = {'A': 3, 'B':1, 'C':2}
    loss_shape = [loss_dic[x] for x in loss_list]

    score = 6*len(win_list) + 3*len(draw_list) + sum(win_shape) + sum(loss_shape) + sum(draw_shape)
    return score

assert calculate_part2(inp_test) == 12
print('Part 2: ',calculate_part2(inp_day2))


