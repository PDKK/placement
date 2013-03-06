#!/usr/bin/python

import unittest
from morseParity import MorseParity
from string import ascii_lowercase




class SanityCheck(unittest.TestCase):
    def setUp(self):
        self.codec = MorseParity()
        


    def testDecode(self):
        for c in ascii_lowercase:
            self.assertEqual(c, self.codec.decode(self.codec.encode(c)))

    def testUppercase(self):
        for c in ascii_lowercase:
            self.assertEqual(c, self.codec.decode(self.codec.encode(c.upper())))

    def testBitFailure(self):
        for c in ascii_lowercase:
            encoded = self.codec.encode(c)
            for bit in range(len(encoded)):
                badEncode = encoded
                if badEncode[bit] == '.':
                    badEncode = badEncode[:bit] + '-' + badEncode[bit+1:]
                else:
                    badEncode = badEncode[:bit] + '.' + badEncode[bit+1:]
                self.assertEqual("?", self.codec.decode(badEncode))

if __name__ == '__main__':
    unittest.main()
