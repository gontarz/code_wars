"""Esoteric languages are pretty hard to program, but it's fairly interesting to write interpreters for them!

Your task is to write a method which will interpret Befunge-93 code! Befunge-93 is a language in which the code is presented not as a series of instructions, but as instructions scattered on a 2D plane; your pointer starts at the top-left corner and defaults to moving right through the code. Note that the instruction pointer wraps around the screen! There is a singular stack which we will assume is unbounded and only contain integers. While Befunge-93 code is supposed to be restricted to 80x25, you need not be concerned with code size. Befunge-93 supports the following instructions (from Wikipedia):

0-9 Push this number onto the stack.
+ Addition: Pop a and b, then push a+b.
- Subtraction: Pop a and b, then push b-a.
* Multiplication: Pop a and b, then push a*b.
/ Integer division: Pop a and b, then push b/a, rounded down. If a is zero, push zero.
% Modulo: Pop a and b, then push the b%a. If a is zero, push zero.
! Logical NOT: Pop a value. If the value is zero, push 1; otherwise, push zero.
` (backtick) Greater than: Pop a and b, then push 1 if b>a, otherwise push zero.
> Start moving right.
< Start moving left.
^ Start moving up.
v Start moving down.
? Start moving in a random cardinal direction.
_ Pop a value; move right if value = 0, left otherwise.
| Pop a value; move down if value = 0, up otherwise.
" Start string mode: push each character's ASCII value all the way up to the next ".
: Duplicate value on top of the stack. If there is nothing on top of the stack, push a 0.
\ Swap two values on top of the stack. If there is only one value, pretend there is an extra 0 on bottom of the stack.
$ Pop value from the stack and discard it.
. Pop value and output as an integer.
, Pop value and output the ASCII character represented by the integer code that is stored in the value.
# Trampoline: Skip next cell.
p A "put" call (a way to store a value for later use). Pop y, x and v, then change the character at the position (x,y) in the program to the character with ASCII value v.
g A "get" call (a way to retrieve data in storage). Pop y and x, then push ASCII value of the character at that position in the program.
@ End program.
(i.e. a space) No-op. Does nothing.
The above list is slightly modified: you'll notice if you look at the Wikipedia page that we do not use the user input instructions and dividing by zero simply yields zero.
"""
import random


def interpret(code):
    output = ""
    # stack = Stack()
    # matrix = DataTable(code)
    output = Run(code).run()
    # TODO: Interpret the code!
    return output


class Run:
    def __init__(self, code):
        self.stack = Stack()
        self.matrix = DataTable(code)
        # print(self.matrix.matrix)
        self.output = ''
        self.bind = {'0': self.stack.push,
                     '1': self.stack.push,
                     '2': self.stack.push,
                     '3': self.stack.push,
                     '4': self.stack.push,
                     '5': self.stack.push,
                     '6': self.stack.push,
                     '7': self.stack.push,
                     '8': self.stack.push,
                     '9': self.stack.push,
                     '+': self.stack.addition,
                     '-': self.stack.subtraction,
                     '*': self.stack.multiplication,
                     '/': self.stack.integer_division,
                     '%': self.stack.modulo,
                     '!': self.stack.logical_not,
                     '`': self.stack.backtrick,
                     '>': self.matrix.assign_right,
                     '<': self.matrix.assign_left,
                     '^': self.matrix.assign_up,
                     'v': self.matrix.assign_down,
                     '?': self.matrix.assign_random,
                     '_': self.underscore,
                     '|': self.pipe,
                     '"': self.string_mode,
                     ':': self.stack.duplicate,
                     '\\': self.stack.swap,
                     '$': self.stack.pop,
                     '.': self.int_output,
                     ',': self.str_output,
                     '#': self.matrix.skip,
                     'p': self.put_call,
                     'g': self.get_call,
                     '@': self.end,
                     ' ': self.space
                     # "'": self.stack.push_ascii
                     }

    def string_mode(self):
        """remember to move before and after string mode"""
        self.matrix.move()
        value = self.matrix.get_pointing_value()
        while value != '"':
            self.stack.push(ord(value))
            self.matrix.move()
            value = self.matrix.get_pointing_value()

    def put_call(self):
        y = self.stack.pop()
        x = self.stack.pop()
        v = self.stack.pop()
        self.matrix.matrix[(x,y)] = chr(v)

    def get_call(self):
        y = self.stack.pop()
        x = self.stack.pop()
        self.stack.push(ord(self.matrix.matrix[(x,y)]))

    def underscore(self):
        a = self.stack.pop()
        self.matrix.move = self.matrix.move_right if a == 0 else self.matrix.move_left

    def pipe(self):
        a = self.stack.pop()
        self.matrix.move = self.matrix.move_down if a == 0 else self.matrix.move_up

    def int_output(self):
        a = self.stack.pop()
        self.output += str(a)

    def str_output(self):
        a = self.stack.pop()
        self.output += chr(a)

    def end(self):
        return self.output
        exit()

    @staticmethod
    def space():
        return

    def run(self):
        while True:
            instruction = self.matrix.get_pointing_value()
            print(instruction)
            print(self.matrix.pointer.pointer)
            if instruction == '@':
                return self.output

            instruction_func = self.bind[instruction]
            if instruction.isdigit():
                instruction_func(instruction)
            else:
                instruction_func()
            self.matrix.move()
            # print(self.matrix.pointer.pointer)
            print(self. output, self.stack.items)


class Pointer:
    def __init__(self, max_x, max_y):
        self.pointer = (0, 0)
        self.max_x = max_x
        self.max_y = max_y

    def update(self, x=None, y=None):
        x1,y1 = self.pointer

        if x is not None:
            x2 = x1+x
            if x2 < 0:
                x2 = self.max_x
            elif x2 > self.max_x:
                x2=0
            self.pointer = (x2, y1)

        elif y is not None:
            y2 = y1 + y
            if y2 < 0:
                y2 = self.max_y
            elif y2 > self.max_x:
                y2=0
            self.pointer = (x1, y2)

    def asign(self, x, y):
        self.pointer = (x, y)

    def get(self):
        return self.pointer[0], self.pointer[1]


class DataTable:
    def __init__(self, code):
        # self.matrix = [list(y) for y in code.split('\n')]
        self.matrix, self.max_x, self.max_y = self.create_matrix(code)
        self.pointer = Pointer(self.max_x, self.max_y)
        self.move = self.move_right

    def create_matrix(self, code):
        matrix = dict()
        prepared = code.split('\n')

        max_x = x = y = 0
        max_y = len(prepared)-1

        for line in prepared:
            for instruction in line:
                matrix[(x,y)] = instruction
                if x > max_x:
                    max_x = x
                x+=1
            x=0
            y+=1
        return matrix, max_x, max_y

    def assign_left(self):
        self.move = self.move_left

    def assign_right(self):
        self.move = self.move_right

    def assign_up(self):
        self.move = self.move_up

    def assign_down(self):
        self.move = self.move_down

    def assign_random(self):
        self.move = random.choice([self.move_left, self.move_right, self.move_up, self.move_down])

    def move_left(self):
        self.pointer.update(x=-1)

    def move_right(self):
        self.pointer.update(x=1)

    def move_up(self):
        self.pointer.update(y=-1)

    def move_down(self):
        self.pointer.update(y=1)

    def skip(self):
        self.move()

    def get_pointing_value(self):
        x, y = self.pointer.get()
        # print(x,y)
        return self.matrix.get((x,y),' ')


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(int(item))

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __repr__(self):
        return ''.join(map(str, self.items))

    def __str__(self):
        return ''.join(map(chr, self.items))

    def pop_a_b(self):
        return self.pop(), self.pop()

    def addition(self):
        self.push(self.pop() + self.pop())

    def subtraction(self):
        a, b = self.pop_a_b()
        self.push(b - a)

    def multiplication(self):
        self.push(self.pop() * self.pop())

    def integer_division(self):
        a, b = self.pop_a_b()
        self.push(b // a) if b != 0 else self.push(b)

    def modulo(self):
        a, b = self.pop_a_b()
        self.push(b % a) if b != 0 else self.push(b)

    def logical_not(self):
        a = self.pop()
        self.push(1) if a == 0 else self.push(0)

    def backtrick(self):
        a, b = self.pop_a_b()
        self.push(1) if b > a else self.push(0)

    def duplicate(self):
        if self.is_empty() is True:
            self.push(0)
        self.push(self.peek())

    def swap(self):
        if self.size() == 1:
            self.push(0)
        else:
            a, b = self.pop_a_b()
            self.push(a)
            self.push(b)


if __name__ == '__main__':
    with open('/home/eustachy/projekty_python/code_wars/Befunge_93_interpreter/befunge_script5.txt') as f:
        code = f.read()
        print(code)
    out = interpret(code)
    print(out)
