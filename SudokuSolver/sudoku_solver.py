# -*- coding: utf-8 -*-
"""
Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
# Should return
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]
"""


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    solve = Puzzle(puzzle)

    while True:
        solve.solve_puzzle()
        if solve.check_all():
            break
    solve.update_puzzle()
    return solve.puzzle[:]


class Puzzle:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.puzzle_dict = self.create_puzzle_dict()
        self.side_len = 9

    def create_puzzle_dict(self):
        return {(x, y): val
                for y, row in enumerate(self.puzzle)
                for x, val in enumerate(row)}

    def update_puzzle(self):
        for k, v in self.puzzle_dict.items():
            self.puzzle[k[1]][k[0]] = v

    def check_row(self, y, value):
        for x in range(self.side_len):
            if value == self.puzzle_dict[(x, y)]:
                return False
        return True

    def check_column(self, x, value):
        for y in range(self.side_len):
            if value == self.puzzle_dict[(x, y)]:
                return False
        return True

    def check_subgid(self, x, y, value):
        first_col = y - y % 3
        last_col = first_col + 3

        first_row = x - x % 3
        last_row = first_row + 3
        for x in range(first_row, last_row):
            for y in range(first_col, last_col):
                if value == self.puzzle_dict[(x, y)]:
                    return False
        return True

    def check_value(self, x, y, value):
        if (
                self.check_subgid(x, y, value)
                and self.check_row(y, value)
                and self.check_column(x, value)
        ):
            return True
        return False

    def check_all(self):
        for k, v in self.puzzle_dict.items():
            if v == 0:
                return False
        return True

    def solve_puzzle(self):
        low_x = low_y = 0
        step = 3
        for y in range(low_y, self.side_len, step):
            for x in range(low_x, self.side_len, step):
                # generated first tuple of each subgrid
                # print('x:%s\ty:%s' %(x,y))
                check_dict = dict()

                # now iter subgrid
                for sub_y in range(x, x + step):
                    for sub_x in range(y, y + step):
                        # print('x:%s\ty:%s' % (sub_x, sub_y), self.puzzle_dict[(sub_x, sub_y)])
                        # continue when filed if solved
                        if self.puzzle_dict[(sub_x, sub_y)] != 0:
                            continue

                        # iter types
                        for val in range(1, 10):
                            if (check_dict.get(val, True) and self.check_value(sub_x, sub_y, val)):
                                check_dict[val] = False if val in check_dict else (sub_x, sub_y)
                # print(check_dict)

                for k, v in check_dict.items():
                    if v:
                        self.puzzle_dict[v] = k
        low_x += 3


if __name__ == '__main__':
    from pprint import pprint

    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    pprint(sudoku(puzzle))
