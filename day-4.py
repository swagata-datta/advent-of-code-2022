'''Day 4: Duplicate cleaning area

https://adventofcode.com/2022/day/4'''

# part 1

from toolkit import *

test_inp = inputfile('input_files/test_files/day-4.txt')
day4_inp = inputfile('input_files/day-4.txt')
def treat_inp(input_f):
    """Turns each element of the list into list containing two elements"""
    inp = [x.split(',') for x in input_f]

    return inp

def is_subset(int1,int2):
    """given two closed intervals, returns if one is a subset of another
    
    interval in the form 'a-b'"""

    # sees if the first interval is a subset of the second
    if (int(int1.split('-')[0]) >= int(int2.split('-')[0]) and int(int1.split('-')[-1]) <= int(int2.split('-')[-1])):
        return True    
    # sees if the second interval is a subset of the first
    elif (int(int2.split('-')[0]) >= int(int1.split('-')[0]) and int(int2.split('-')[-1]) <= int(int1.split('-')[-1])):
        return True
    else:
        return False

assert is_subset('58-64','59-65') == False
assert is_subset('3-4','1-7') == True
assert is_subset('2-5','3-6') == False
assert is_subset('3-4','3-4') == True
def part1(inp):
    """will find the number of times one assignment is contained in another"""
    inp = treat_inp(inp)
    score = sum([is_subset(x[0],x[1]) for x in inp])

    return score

assert part1(test_inp) == 2
print('Part 1: ', part1(day4_inp))