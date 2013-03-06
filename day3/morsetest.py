import unittest
from morse import Morse
from string import ascii_lowercase




class SanityCheck(unittest.TestCase):
    def setUp(self):
        self.morse = Morse()
        

    def testEncodeA(self):
        self.assertEqual(".-", self.morse.encode("a"))
    def testEncodeB(self):
        self.assertEqual("-...", self.morse.encode("b"))
    def testEncodeC(self):
        self.assertEqual("-.-.", self.morse.encode("c"))
    def testEncodeD(self):
        self.assertEqual("-..", self.morse.encode("d"))
    def testEncodeE(self):
        self.assertEqual(".", self.morse.encode("e"))
    def testEncodeF(self):
        self.assertEqual("..-.", self.morse.encode("f"))
    def testEncodeG(self):
        self.assertEqual("--.", self.morse.encode("g"))
    def testEncodeH(self):
        self.assertEqual("....", self.morse.encode("h"))
    def testEncodeI(self):
        self.assertEqual("..", self.morse.encode("i"))
    def testEncodeJ(self):
        self.assertEqual(".---", self.morse.encode("j"))
    def testEncodeK(self):
        self.assertEqual("-.-", self.morse.encode("k"))
    def testEncodeL(self):
        self.assertEqual(".-..", self.morse.encode("l"))
    def testEncodeM(self):
        self.assertEqual("--", self.morse.encode("m"))
    def testEncodeN(self):
        self.assertEqual("-.", self.morse.encode("n"))
    def testEncodeO(self):
        self.assertEqual("---", self.morse.encode("o"))
    def testEncodeP(self):
        self.assertEqual(".--.", self.morse.encode("p"))
    def testEncodeQ(self):
        self.assertEqual("--.-", self.morse.encode("q"))
    def testEncodeR(self):
        self.assertEqual(".-.", self.morse.encode("r"))
    def testEncodeS(self):
        self.assertEqual("...", self.morse.encode("s"))
    def testEncodeT(self):
        self.assertEqual("-", self.morse.encode("t"))
    def testEncodeU(self):
        self.assertEqual("..-", self.morse.encode("u"))
    def testEncodeV(self):
        self.assertEqual("...-", self.morse.encode("v"))
    def testEncodeW(self):
        self.assertEqual(".--", self.morse.encode("w"))
    def testEncodeX(self):
        self.assertEqual("-..-", self.morse.encode("x"))
    def testEncodeY(self):
        self.assertEqual("-.--", self.morse.encode("y"))
    def testEncodeZ(self):
        self.assertEqual("--..", self.morse.encode("z"))

    def testDecode(self):
        for c in ascii_lowercase:
            self.assertEqual(c, self.morse.decode(self.morse.encode(c)))

    def testUppercase(self):
        for c in ascii_lowercase:
            self.assertEqual(c, self.morse.decode(self.morse.encode(c.upper())))

if __name__ == '__main__':
    unittest.main()
