import unittest
from common import fetch_challenge_input
from requests import HTTPError


class TestInputFetching(unittest.TestCase):
    def test_fetch_input_from_day_one(self):
        challenge_input = fetch_challenge_input(1)
        self.assertIsNotNone(challenge_input)

    def test_fetch_input_from_invalid_day(self):
        with self.assertRaises(HTTPError):
            fetch_challenge_input(100)


if __name__ == '__main__':
    unittest.main()
