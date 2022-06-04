# test_str.py
import unittest
import my_utils

@my_utils.my_async
def A():
    print("函数A睡了。。。。。。")
    print("a function")


def B():
    print("b function")

class TestUtilsMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_my_async(self):
        B()
        A()
        print("finish")

if __name__ == '__main__':
    unittest.main()

# python test_utils.py
