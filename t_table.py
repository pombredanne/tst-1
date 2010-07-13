'''
Cactus - The Python Task Runner
Author: Tim Henderson
Contact: tim.tadh@hackthology.com
Copyright (c) 2010 All Rights Reserved.
Licensed under a BSD style license see the LICENSE file.
'''
import unittest
from table import match_globs, SymbolTable
class TestMatchGlobs(unittest.TestCase):
	
	def test_match(self):
		tests = [('ab*cd', 'abcd', True), ('ab*cd', 'abedcd', True), 
				('ab*cd', 'abed*cd', True),
				('ab*cd', 'ab*edcd', True),
				('ab*cd', 'a*edcd', True),
				('ab*cd', 'acd', False),
				('abc*cd', 'ad', False),
				('*cd', 'abcd', True),
				('abcd', 'ab*', True),
				('ab*', '*', True), 
				('ab*', '*cd', True),
				('abc*cd*', 'a*xy*', True),
				('ab*ac*c', '*ab*cd', False)]
		for test in tests:
			if test[0]: m = 'matched'
			else: m = 'not matched'
			self.assert_(match_globs(test[0], test[1]) == test[2], '"%s" and "%s" should have %s' % (test[0], test[1], m))

if __name__ == '__main__':
	unittest.main()