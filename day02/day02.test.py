import unittest
import day02

class Day02Tests(unittest.TestCase):

    def test_partOne_TestInput(self):
        self.assertEqual(day02.part1(day02.testInputPartOne), 8)

    def test_partOne_PuzzleInput(self):
        self.assertEqual(day02.part1(day02.puzzleInput), 2716)

if __name__ == '__main__':
    unittest.main()
            