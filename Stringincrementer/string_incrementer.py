# -*- coding: utf-8 -*-


def increment_string(strng):
    if strng and strng[-1].isdigit():
        if strng.isdigit():
            return str(int(strng) + 1).zfill(len(strng))
        digit_index = find_digit(strng)
        digit = strng[digit_index:]
        print(digit,digit_index)
        return strng[:digit_index] + str(int(digit) + 1).zfill(len(digit))
    else:
        return strng + '1'


def find_digit(s):
    for i, c in enumerate(reversed(s)):
        print(i,c)
        if c.isdigit() is False:
            return len(s) - i


if __name__ == '__main__':
    s = increment_string('x6xx099')
    print(s)
