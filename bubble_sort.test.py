import unittest  # https://docs.python.org/2/library/unittest.html
import bubble_sort


class BubbleSortMethods(unittest.TestCase):

    def test_variant_1(self):
        self.assertEqual([1, 2, 3], bubble_sort.sort_1([3, 2, 1]))

    def test_variant_2(self):
        self.assertEqual([1, 2, 3], bubble_sort.sort_2([3, 2, 1]))

if __name__ == '__main__':
    unittest.main()
