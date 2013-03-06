#!/usr/bin/python

import unittest
from fiveBitCodec import FiveBitCodec
from string import ascii_lowercase



class SanityCheck(unittest.TestCase):
    def setUp(self):
        self.codec = FiveBitCodec()
        
    def testEncode(self):
      
      for c in ascii_lowercase:
        testValue = ""
        val = ord(c)- ord('a')
        for i in range(5):
          if val & 1 << i:
            testValue = '-' + testValue
          else:
            testValue = '.' + testValue
        self.assertEqual(testValue, self.codec.encode(c))

    def testLength(self):
      self.assertEqual('?',self.codec.decode('......'))
      self.assertEqual('?',self.codec.decode('....'))
      self.assertEqual('?',self.codec.decode('...'))
      self.assertEqual('?',self.codec.decode('..'))
      self.assertEqual('?',self.codec.decode('.'))
      
    def testSpace(self):
		self.assertEqual(' ',self.codec.decode('--.-.'))
		self.assertEqual('--.-.',self.codec.encode(' '))


    def testDecode(self):
        for c in ascii_lowercase:
            self.assertEqual(c, self.codec.decode(self.codec.encode(c)))

    def testUppercase(self):
        for c in ascii_lowercase:
            self.assertEqual(c, self.codec.decode(self.codec.encode(c.upper())))


if __name__ == '__main__':
    unittest.main()
