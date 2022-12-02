'''Day 1 puzzle

From https://adventofcode.com/2022/day/1'''

# part 1

from toolkit import *

test_inp=inputfile("input_files/test_files/day-1.txt", lines=False) 

def get_max_cal(input_f):
    """Gets the maximum value of the calorie that an individual elf has"""
    separate_elf=input_f.split("\n\n") # this separates the elfs and creates a list
    sep_elf=[turn_list_to_int(x.split()) for x in separate_elf] # this creates nested list with the calorie numbers

    add_cal=[sum(x) for x in sep_elf] # list of total calories
    cal=set(add_cal)
    return max(cal)

assert get_max_cal(test_inp) ==24000

day_1_inp=inputfile("input_files/day-1.txt", lines=False)
print(get_max_cal(day_1_inp))

#===================
# part 2
# need addition of top 3
def top_three(input_f):
    separate_elf=input_f.split("\n\n") # this separates the elfs and creates a list
    sep_elf=[turn_list_to_int(x.split()) for x in separate_elf] # this creates nested list with the calorie numbers

    add_cal=[sum(x) for x in sep_elf] # list of total calories
    sorted_cal = sorted(add_cal)

    return sum(sorted_cal[-3:])


assert top_three(test_inp) == 45000

print(top_three(day_1_inp))
