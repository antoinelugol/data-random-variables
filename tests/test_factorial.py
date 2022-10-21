from nbresult import ChallengeResultTestCase

class TestFactorial(ChallengeResultTestCase):

    # Test for count_possibilities
    def test_count_possibilities_11(self):
        expected = 1
        self.assertEqual(self.result.count_possibilities_11, expected)
    
    def test_count_possibilities_43(self):
        expected = 4
        self.assertEqual(self.result.count_possibilities_43, expected)

    def test_count_total_possibilities_10(self):
        expected = 1024
        self.assertEqual(self.result.count_total_possibilities_10, expected)

    def test_probability_1(self):
        expected = {0: 0.5, 1: 0.5}
        self.assertEqual(self.result.probability_1, expected)

    def test_probability_100(self):
        expected = 0.08
        self.assertAlmostEqual(self.result.probability_100[50], expected, places=2)


