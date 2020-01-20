import math
import numpy as np

BASE = 3
PRECISION = 5
L = -3
U = +3
# We will represent a floating number as a tuple (mantissa, exponent, sign)
# With: mantissa -- a list of integers of length PRECISION
# exponent -- an integer between L and U (inclusive)
# sign -- either 1 or -1
example_float = ([1, 0, 0, 1, 0], 1, 1)


def is_valid_mantissa(int_lst,float_value):
    if int_lst[0] == 0 and float_value == 0:
        for x in int_lst[1:]:
            if x >= base or x<1:
                return False
    else:
        for x in int_lst:
            if x >= base or x<1:
                return False
    return True



def is_valid_float(float_value):

    (mantissa, exponent, sign) = float_value
    return len(mantissa) == PRECISION and is_valid_mantissa(mantissa) and (exponent <= U and exponent >= L) and (sign == 1 or sign == -1)


largest_negative = ([2,2,2,2,2], 3,-1)
smallest_positive = ([1,0,0,0,1], -3, 1)
float_32 = ([], None, None)


def to_num(float_value):
    
    (mantissa, exponent, sign) = float_value
    sum_mantissa = 0
    for i in range(len(mantissa)):
        sum_mantissa += mantissa[i] / math.pow(3,i)
    
    return sum_mantissa * math.pow(3,exponent)*sign


def add_float(float1, float2):
    """Return a valid floating-point representation of the form (mantissa, exponent, sign)
    that is the sum of `float1` and `float2`. Raises a ValueError if the result of
    the addition is not a valid float.
    2
    >>> add_float(example_float, example_float)
    ([2, 0, 0, 2, 0], 1, 1])
    """
    
    (mantissa1, exponent1, sign1) = float1
    (mantissa2, exponent2, sign2) = float2


    # You may assume that sign1 and sign2 are positive
    assert (sign1 == 1) and (sign2 == 1)
    max_expo = exponent1
    shift = 0
    if exponent2 > exponent1:
        temp = []
        shift = exponent2 - exponent1
        temp = mantissa1
        mantissa1 = mantissa2
        mantissa2 = temp
        max_expo = exponent2
    else:
        shift = exponent1 - exponent2
    
    if shift >= PRECISION:
        return (mantissa1, max_expo, 1)

    #float 1 exp >= float 2 exp
    carry = 0
    i = 0 
    lim = 5 - shift 
    res = []
    print(shift)
    while(i < PRECISION):
        store = 0
        if i < lim:
            print(str(mantissa1[PRECISION - 1 - i]) + '+' + str(mantissa2[PRECISION-1-i]))
            sums = mantissa1[PRECISION - 1 - i] + mantissa2[PRECISION-1-i] + carry
            carry = sums // BASE
            store = sums%BASE
        else:
            sums = mantissa1[i1] + carry
            carry = sums%BASE
            store = sums // BASE
        res = [store] + res
        print(res)
        i+=1

        


    # Add your code here
    return (res, max_expo, 1)

v = add_float(example_float, example_float)

print(v)