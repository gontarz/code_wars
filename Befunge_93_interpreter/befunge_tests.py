from .Befunge_93_interpreter import DataTable, Run, Stack

import unittest


class TestDataTable(unittest.TestCase):
    def test_matrix1(self):
        table = DataTable('>987v>.v\nv456<  :\n>321 ^ _@')
        test_data = table.matrix
        # print(table.matrix)
        out_data = {(0, 0): '>', (1, 0): '9', (2, 0): '8', (3, 0): '7', (4, 0): 'v', (5, 0): '>', (6, 0): '.',
                    (7, 0): 'v',
                    (0, 1): 'v', (1, 1): '4', (2, 1): '5', (3, 1): '6', (4, 1): '<', (5, 1): ' ', (6, 1): ' ',
                    (7, 1): ':',
                    (0, 2): '>', (1, 2): '3', (2, 2): '2', (3, 2): '1', (4, 2): ' ', (5, 2): '^', (6, 2): ' ',
                    (7, 2): '_',
                    (8, 2): '@'}

        self.assertEqual(test_data, out_data)

    def test_matrix2(self):
        table = DataTable('>987v>.v\nv456<  :\n>321     ')
        in_data = table.matrix
        # print(table.matrix)
        out_data = {(0, 0): '>', (1, 0): '9', (2, 0): '8', (3, 0): '7', (4, 0): 'v', (5, 0): '>', (6, 0): '.',
                    (7, 0): 'v',
                    (0, 1): 'v', (1, 1): '4', (2, 1): '5', (3, 1): '6', (4, 1): '<', (5, 1): ' ', (6, 1): ' ',
                    (7, 1): ':',
                    (0, 2): '>', (1, 2): '3', (2, 2): '2', (3, 2): '1', (4, 2): ' ', (5, 2): ' ', (6, 2): ' ',
                    (7, 2): ' ',
                    (8, 2): ' '}

        self.assertEqual(in_data, out_data)


class TestInterpreter(unittest.TestCase):
    def test_run(self):
        test_run = Run('>987v>.v\nv456<  :\n>321 ^ _@').run()
        assertion = '123456789'
        self.assertEqual(test_run, assertion)

    def test_run2(self):
        test_run = Run('>64+"!dlroW ,olleH">:#,_@').run()
        assertion = 'Hello, World!%s'% chr(10)
        self.assertEqual(test_run, assertion)

    def test_run3(self):
        test_run = Run(':0g,:93+`#@_1+').run()
        assertion = ':0g,:93+`#@_1+'
        self.assertEqual(test_run, assertion)

    def test_run4(self):
        test_run = Run('01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@').run()
        assertion = '01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@'
        self.assertEqual(test_run, assertion)


class TestStack(unittest.TestCase):
    def test_duplicate(self):
        stack = Stack()
        stack.duplicate()
        self.assertEqual(stack.items, [0,0])


if __name__ == '__main__':
    unittest.main()


