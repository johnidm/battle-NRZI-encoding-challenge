import unittest

from nrzi_encoding import NRZI


class TestNRZIEncoding(unittest.TestCase):

    def test_encoding(self):
        _expected = ('010010000100111', '010110010', '010011000110')
        _input = ('¯|___|¯¯¯¯¯|___|¯|_|¯', '¯|__|¯|___|¯¯', '_|¯¯¯|_|¯¯¯¯|_|¯¯')
        
        for _in, _out in zip(_input, _expected):
            self.assertEqual(NRZI().econding(_in), _out) 

if __name__ == "__main__":
    unittest.main()