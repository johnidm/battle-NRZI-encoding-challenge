import unittest

from nrzi_encoding import nrzi


class TestNRZIEncoding(unittest.TestCase):

    def test_encoding(self):
        _expected = (
            '010010000100111', '010110010', '010011000110', '010100011101')
        _input = ('¯|___|¯¯¯¯¯|___|¯|_|¯', '¯|__|¯|___|¯¯',
                  '_|¯¯¯|_|¯¯¯¯|_|¯¯', '_|¯¯|____|¯|_|¯¯|_')

        for _in, _out in zip(_input, _expected):
            self.assertEqual(nrzi(_in), _out)

    def test_encoding_one_singal(self):
        self.assertEqual(nrzi('_'), '0')
        self.assertEqual(nrzi('_'), '0')
        self.assertEqual(nrzi('¯|'), '0')
        self.assertEqual(nrzi('¯|'), '0')

    def test_econding_transmission_empty(self):
        pass

    def test_econding_transmission_first_signal_invalid(self):
        pass


if __name__ == "__main__":
    unittest.main()
