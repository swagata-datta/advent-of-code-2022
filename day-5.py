'''Day 5: Stacks
December 9 2022

https://adventofcode.com/2022/day/5'''

#part 1
from toolkit import *

# editing the input files, adding 0's where the stack is empty
inp_test = inputfile('input_files/test_files/day-5.txt')
inp_day5 = inputfile('input_files/day-5.txt')

def treat_files(input_f, lines):
    """Returns two list, the stack with the crates and the procedures with movements.
    lines is the line number where the procedures start"""
    
    stack = input_f[:lines]
    procedures = input_f[lines:]

    return stack, procedures

def get_stack(stack_list):
    """Turns the stack list from treat_files function into list of lists, each list representing a column"""
    stack_list.pop()
    stack_list = [i.split() for i in stack_list]

    stack = list_to_arr(stack_list)
    num = len(stack[0])    # number of stacks
    stack_list = []
    for i in range(num):
        st = [x[i][1] for x in stack if x[i] != '0']
        st.reverse()    # I want the top crate to be the last element and so on, therefore, need to reverse the list
        stack_list.append(st)
    
    return stack_list

def get_procedures(procedures):
    """Turns the procedures from treat_files function into list of list of three numbers, [number, from, to]"""
    procedures.remove(procedures[0])    # removing the first element which is blank space
    # each element of procedure is in the form 'move 1 from 2 to 1'
    indices = [1,3,-1]
    proc_list = [[int(i.split()[j]) for j in indices] for i in procedures]

    return proc_list

def restack(stack_list, procedures):
    '''Does the restacking given stack and procedures
    returns the top three crates as a string'''
    for i in procedures:        # iterating over the procedures
        count = i[0]            # number of crates to be moved
        from_ = i[1]            # stack from while crate is taken
        to_ = i[2]              # target stack
        while count != 0:
            count -= 1
            crate = stack_list[from_-1][-1]
            stack_list[from_-1].pop()
            stack_list[to_-1].append(crate)
        
    top = [i[-1] for i in stack_list]
    top = ''.join(top)
    return top
            
def part1(inp, lines):
    stack_list = get_stack(treat_files(inp, lines)[0])
    procedures = get_procedures(treat_files(inp, lines)[1])
    return restack(stack_list, procedures)

assert part1(inp_test,4) == 'CMZ'

print(part1(inp_day5, 9))
