from solution_header import *
import unittest


class Test(unittest.TestCase):
    def testmakeConfidentialStringName(self):
        result = MaskerClass.makeConfidentialString(self,"Osman Onur KUZUCU")
        self.assertEqual(result,"XXXXX XXXX XXXXXX")

    def testmakeConfidentialStringMaik(self):
        result = MaskerClass.makeConfidentialString(self,"kuzucu48@gmail.com")
        self.assertEqual(result,"XXXXXXXX@XXXXX.XXX")


unittest.main()