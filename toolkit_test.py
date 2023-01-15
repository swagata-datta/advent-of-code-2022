"""testing for functions in toolkit.py

Swagata"""

import collections
from toolkit import *
import re
import numpy as np
import pandas as pd


assert binary_to_decimal('10110') == 22
assert binary_to_decimal('01001') == 9

assert str_to_tup('3, 4') == (3,4)
assert str_to_tup('4,5,6') == (4,5,6)


# decimal to binary

def decimal_to_binary(num, bits, indices = []):
    """Takes in a decimal number, and number of bits and returns the binary"""
    def largest_exponent(num):
        """Returns the largest possible exponent of two that goes into the number
        e.g. for 7, the largest possible is 2^2=4. The function will return 2"""
        for i in range(bits):
            if num < 2:
                return i
            elif num / 2 < 2:
                return i + 1
            else:
                num = num / 2
    if num == 0:
        binary = ['0'] * bits
        for i in indices:
            binary[i] = '1'
        binary.reverse()
        final = ''.join(binary)
        return final
    else:
        exp = largest_exponent(num)                                 # the largest exponent of 2 that `goes into` num
        indices.append(exp)  
        num = num - 2 ** exp                                        # new number is what remains
        return decimal_to_binary(num, bits, indices)

