from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        import numpy as np
        res = solution()

        self.assertEqual(res['name']['a'], 'Anastasia')
        self.assertEqual(res['name']['j'], 'Jonas')

        self.assertEqual(res['score']['i'], 8.0)
        self.assertEqual(res['score']['c'], 16.5)
