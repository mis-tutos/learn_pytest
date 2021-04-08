import unittest

class Mis_tests(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(2+2,4)

    def test_resta(self):
        self.assertTrue(1-1==0)

    def test_multi(self):
        self.assertEqual(3*3,9)

if __name__ == '__main__':
    unittest.main()