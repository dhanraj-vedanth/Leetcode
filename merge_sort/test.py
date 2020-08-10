import unittest
from sorterr import Mergesort

class TestMerge(unittest.TestCase):

    def test_mergesort(self):
        merge_obj = Mergesort()
        print(merge_obj.random_array_generator(10,0,50))
        

if __name__ == '__main__':
    unittest.main()

