import unittest
import day01

class Day01Tests(unittest.TestCase):

    def test_partOne_TestInput(self):
        self.assertEqual(day01.part1(day01.testInputPartOne), 142)

    def test_partOne_PuzzleInput(self):
        self.assertEqual(day01.part1(day01.puzzleInput), 53080)

    def test_partTwo_TestInput(self):
        self.assertEqual(day01.part2(day01.testInputPartTwo), 281)

    def test_partTwo_PuzzleInput(self):
        self.assertEqual(day01.part2(day01.puzzleInput), 53268)

    def test_partTwo_ConsecutiveNumbers(self):
        self.assertEqual(day01.parsePureDigitsOrNumbersWrittenInLetters("eighthree"), ["eight", "three"])

if __name__ == '__main__':
    unittest.main()
            