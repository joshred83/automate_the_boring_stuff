import unittest

from comma_code import comma_code


class CommaCodeTest(unittest.TestCase):
    def test_multiple_items(self):
        given = ['apples', 'bananas', 'tofu', 'cats']
        returns = 'apples, bananas, tofu, and cats'

        self.assertEqual(comma_code(given), returns)

    def test_single_item(self):
        given = ['cats']
        returns = 'cats'
        self.assertEqual(comma_code(given), returns)

    def test_no_items(self):
        given = []
        returns = ''

        self.assertEqual(comma_code(given), returns)


if __name__ == '__main__':
    unittest.main()
