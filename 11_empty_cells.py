"""
You are given an integer n representing the length of an n by n board.
Remove all cells that are diagonal to one of the four corners 
(top left, top right, bottom right, and bottom left) and 
return the number of empty cells leftover.

For example, given n = 4

X O O X
O X X O
O X X O
X O O X
We see there's 8 empty "O" squares.

Example 1
Input

n = 4
Output

8
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

# Work out the logic and then code it


def empty_cells(n):
    if n%2==0:
        return n*n-n*2
    else:
        return n*n-n*2+1



# DO NOT TOUCH THE BELOW CODE
class TestEmptyCells(unittest.TestCase):

    def test_01(self):
        self.assertEqual(empty_cells(4), 8)

    def test_02(self):
        self.assertEqual(empty_cells(5), 16)

    def test_03(self):
        self.assertEqual(empty_cells(10), 80)

    def test_04(self):
        self.assertEqual(empty_cells(11), 100)

    def test_05(self):
        self.assertEqual(empty_cells(1), 0)

    def test_06(self):
        self.assertEqual(empty_cells(2), 0)

    def test_07(self):
        self.assertEqual(empty_cells(20), 360)

    def test_08(self):
        self.assertEqual(empty_cells(33), 1024)


if __name__ == '__main__':
    unittest.main(verbosity=2)
