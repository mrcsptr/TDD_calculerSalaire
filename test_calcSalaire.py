# coding: utf-8

import unittest
from calcSalaire import *


class MyFirstTests(unittest.TestCase):

	def testArch(self):
		self.assertEqual(calculerSalaire('architecte', 4), '4000€')

	def testMed(self):
		self.assertEqual(calculerSalaire('médecin', 8), '7000€')

	def testCon(self):
		self.assertEqual(calculerSalaire('consultant', 5), '5000€')






