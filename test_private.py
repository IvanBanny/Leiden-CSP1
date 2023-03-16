import unittest
import numpy as np

from csp import CSP

class TestCSP(unittest.TestCase):
    def test_search_full_problem(self):
        grid = np.array([
            [2, 0, 0],
            [0, 0, 5],
            [0, 0, 0]
        ])
        solution = np.array([
            [2, 2, 2],
            [2, 2, 5],
            [5, 5, 2]
        ])

        groups = [
            [(0, 0), (0, 1), (0, 2)],
            [(0, 2), (1, 2), (2, 2)],
            [(1, 1,), (1, 2)],
            [(1, 0), (1, 1)],
            [(1, 0), (2, 0), (2, 1), (2, 2)]
        ]

        constraints = [(6, 3), (9, 2), (8, 1), (4, 2), (14, 2)]
        set_numbers = {7, 2, 5}

        csp = CSP(grid, set_numbers, groups, constraints)
        search = csp.start_search()
        self.assertTrue(np.all(search == solution))

    def test_search_group_constaint(self):
        grid = np.array([
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 0]
        ])

        groups = [
            [(0, 2), (1, 2), (2, 2)],
            [(1, 0), (2, 0), (2, 1), (2, 2)]
        ]

        constraints = [(4, 1), (8, 2)]
        set_numbers = {3, 1, 5}

        csp = CSP(grid, set_numbers, groups, constraints)
        search = csp.start_search()

        self.assertTrue(search is None)

    def test_search_wrong_input(self):
        grid = np.array([
            [3, 0, 0],
            [0, 0, 5],
            [0, 0, 4]
        ])

        groups = [
            [(0, 0), (0, 1), (0, 2)],
            [(0, 2), (1, 2), (2, 2)],
            [(1, 1,), (1, 2)],
            [(1, 0), (1, 1)],
            [(1, 0), (2, 0), (2, 1), (2, 2)]
        ]

        constraints = [(6, 3), (9, 2), (8, 1), (4, 2), (14, 2)]
        set_numbers = {7, 2, 5}

        csp = CSP(grid, set_numbers, groups, constraints)
        search = csp.start_search()
        self.assertTrue(search is None)

    def test_search_full_problem2(self):
        grid = np.array([
            [0, 0],
            [0, 0],
            [0, 0]
        ])
        solution = np.array([
            [1, 1],
            [1, 1],
            [1, 1]
        ])

        groups = [
            [(0, 1), (1, 1), (2, 1)],
            [(0, 0), (0, 1)],
            [(1, 0)],
            [(1, 0), (1, 1), (2, 0), (2, 1)]
        ]

        constraints = [(3, 3), (2, 2), (1, 1), (4, 4)]
        set_numbers = {1, 3, 2}

        csp = CSP(grid, set_numbers, groups, constraints)
        search = csp.start_search()
        self.assertTrue(np.all(search == solution))

    def test_search_full_greedy(self):
        grid = np.array([
            [0, 0],
            [0, 0]
        ])
        solution = np.array([
            [3, 1],
            [1, 1],
        ])

        groups = [
            [(0, 0), (0, 1)],
            [(0, 1), (1, 1)],
        ]

        constraints = [(4, 1), (2, 2)]
        set_numbers = {1, 3, 5}

        csp = CSP(grid, set_numbers, groups, constraints)
        search = csp.start_search()
        self.assertTrue(np.all(search == solution))

if __name__ == '__main__':
    unittest.main()
    # let's go
