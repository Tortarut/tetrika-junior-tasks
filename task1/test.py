import unittest
from solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

class TaskTestCase(unittest. TestCase):
    def test_only_args(self):
        self.assertEqual(sum_two(1, 2), 3)
        with self.assertRaises(TypeError) as context:
            sum_two(2, 1.4)
        self.assertEqual("Аргумент b должен быть типа <class 'int'>, а не <class 'float'>", str(context.exception))
    
    def test_only_kwargs(self):
        self.assertEqual(sum_two(a=1, b=2), 3)
        with self.assertRaises(TypeError) as context:
            sum_two(a=2, b=1.4)
        self.assertEqual("Ключевой аргумент b должен быть типа <class 'int'>, а не <class 'float'>", str(context.exception))
    
    def test_arg_and_kward(self):
        self.assertEqual(sum_two(1, b=2), 3)
        with self.assertRaises(TypeError) as context:
            sum_two(2, b=1.4)
        self.assertEqual("Ключевой аргумент b должен быть типа <class 'int'>, а не <class 'float'>", str(context.exception))

        with self.assertRaises(TypeError) as context:
            sum_two(1.4, b=2)
        self.assertEqual("Аргумент a должен быть типа <class 'int'>, а не <class 'float'>", str(context.exception))

if __name__=='__main__':
    unittest.main()    