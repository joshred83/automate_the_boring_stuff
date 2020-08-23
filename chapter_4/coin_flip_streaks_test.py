import unittest

import coin_flip_streaks


class MyTestCase(unittest.TestCase):
    def test_flip_coin(self):
        self.assertIn(coin_flip_streaks.flip_coin(), ['H', 'T'])

    def test_flip_n_once(self):
        self.assertEqual(len(coin_flip_streaks.flip_n(1)), 1)

    def test_flip_n_five_times(self):
        self.assertEqual(len(coin_flip_streaks.flip_n(5)), 5)

    def test_flip_n_100_times_only_heads_tails(self):
        flips = coin_flip_streaks.flip_n(100)
        self.assertIn('H', flips)
        self.assertIn('T', flips)

    # def test_flip_n_100_times_seems_random(self):
    #     flips = coin_flip_streaks.flip_n(500)
    #     heads = len([h for h in flips if h == 'H'])
    #     tails = len([t for t in flips if t == 'T'])
    #     self.assertAlmostEqual(heads / tails, 1, msg="Weird ratio, {heads/tails}", delta=0.50)
    #     self.assertNotEqual(heads - tails, 0, msg="Too perfect, {heads/tails}")

    def test_count_streaks_returns_zero(self):
        input = ['H', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'H', 'T']
        self.assertEqual(coin_flip_streaks.count_streaks(input), 0)

    def test_count_streaks_returns_one(self):
        input = ['H', 'H', 'H', 'H', 'H', 'H', 'T']
        self.assertEqual(coin_flip_streaks.count_streaks(input), 1)

    def test_count_streaks_returns_two(self):
        input = ['H', 'H', 'H', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'T']
        self.assertEqual(coin_flip_streaks.count_streaks(input), 2)

    def test_count_streaks_returns_two(self):
        input = ['H', 'H', 'H', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'T']
        self.assertEqual(coin_flip_streaks.count_streaks(input), 2)

    def test_count_streaks_long_streak_counts_once(self):
        input = ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H',
                 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H',
                 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(coin_flip_streaks.count_streaks(input), 1)


if __name__ == '__main__':
    unittest.main()
