import unittest
from common import fetch_challenge_input
from day01 import qone, qtwo


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        inputs = list(map(int, fetch_challenge_input(1)))
        res = qone(inputs)
        print(f"solution 1 : {res}")
        self.assertIsInstance(res, int)

    def test_part_two(self):
        inputs = list(map(int, fetch_challenge_input(1)))
        res = qtwo(inputs)
        print(f"solution 2 : {res}")
        self.assertIsInstance(res, int)


if __name__ == '__main__':
    unittest.main()
