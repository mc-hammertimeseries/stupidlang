import unittest
from pytest import raises
from .parser import typer, lex, syn, parse

class ParserTest(unittest.TestCase):

	def setUp(self):
		self.simpleEqn = '(+ 2 3)'
		self.nestedEqn = '(+ 2 (* 3 true))'
		self.simpleList = ['(', '+', 2, 3, ')']
		self.nestedList = ['(', '+', 2, '(', '*', 3, True, ')', ')']

	def test_typer(self):
		self.assertEqual(typer('true'), True)
		self.assertEqual(typer('false'), False)
		self.assertEqual(typer('3'), 3)
		self.assertEqual(typer('3.7'), 3.7)
		self.assertEqual(typer('abc'), 'abc')

	def test_lex(self):
		self.assertEqual(lex(self.simpleEqn), ['(', '+', 2, 3, ')'])
		self.assertEqual(lex(self.nestedEqn), ['(', '+', 2, '(', '*', 3, True, ')', ')'])

	def test_syn(self):
		self.assertEqual(syn(self.simpleList), ['+', 2, 3])
		self.assertEqual(syn(self.nestedList), ['+', 2, ['*', 3, True]])
		self.assertEqual(syn(''), [])

	def test_parse(self):
		self.assertEqual(parse(self.nestedEqn), ['+', 2, ['*', 3, True]])
		with self.assertRaises(AssertionError):
			parse(')')