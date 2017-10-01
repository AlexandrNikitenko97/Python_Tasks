"""
 In our version of multiplication, we convert numbers to binary representation without leading zeroes.
 Then the first number is written vertically (up to down) and the second horizontally (left to right).
 With that, we fill a table with various binary operations for each crossing -- AND, OR, XOR, so we end up with three
 tables.
 In each table we convert rows to decimal and summarize it, then summarize the results of three tables.

You are given two positive integers (n > 0), be careful with order of arguments.

Input: Two arguments as integers.

Output: The result of the Stephan's "multiplication", an integer.

Example:

mul(4, 6) == 38

mul(2, 7) == 28

mul(7, 2) == 18

"""


def mul(first, second):
    first, second = bin(first).lstrip('0b'), bin(second).lstrip('0b')
    num_and = num_or = num_xor = 0
    for i in first:
        number_and = number_or = number_xor = ''
        for j in second:
            number_and += str(int(i) and int(j))
            number_or += str(int(i) or int(j))
            number_xor += str(int(i) ^ int(j))
            if len(number_and) == len(second):
                num_and += int(number_and, 2)
                num_or += int(number_or, 2)
                num_xor += int(number_xor, 2)
    return num_and + num_or + num_xor
