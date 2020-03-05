# @File  : Test_TwoStack.py
# @Author: Magic Huang
# @GitHub: github.com/MH-Blog
# @Date  : 2020/3/5

import unittest

from TwoStack import TwoStack


class TestTwoStack(unittest.TestCase):
    def test_init(self):
        stack = TwoStack(5)
        self.assertEqual(stack.size1, 0)
        self.assertEqual(stack.size2, 4)

    def test_l_num(self):
        stack = TwoStack(5)
        stack.l_push(1)
        self.assertEqual(stack.l_num(), 1)

    def test_r_num(self):
        stack = TwoStack(5)
        stack.r_push(1)
        self.assertEqual(stack.r_num(), 1)

    def test_isEmpty1(self):
        stack = TwoStack(5)
        self.assertEqual(stack.isEmpty1(), True)

    def test_isEmpty2(self):
        stack = TwoStack(5)
        stack.r_push(1)
        self.assertEqual(stack.isEmpty2(), False)

    def test_capacity(self):
        stack = TwoStack(5)
        self.assertEqual(stack.capacity(), 5)

    def test_ensure_capacity(self):
        stack = TwoStack(5)
        for i in range(6):
            stack.l_push(i)
        self.assertEqual(stack.capacity(), 10)

    def test_l_push(self):
        stack = TwoStack(5)
        self.assertEqual(stack.l_push(1), [1, None, None, None, None])

    def test_r_push(self):
        stack = TwoStack(5)
        self.assertEqual(stack.r_push(1), [None, None, None, None, 1])

    def test_l_pop(self):
        stack = TwoStack(5)
        with self.assertRaises(AttributeError):
            value = stack.l_pop()

    def test_r_pop(self):
        stack = TwoStack(5)
        with self.assertRaises(AttributeError):
            value = stack.r_pop()


if __name__ == '__main__':
    unittest.main()
