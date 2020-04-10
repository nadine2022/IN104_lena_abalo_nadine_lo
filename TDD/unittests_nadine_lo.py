import unittest
import zoo

class BadInput(unittest.TestCase):

    def test_species(self):
        """the species are Asian or African"""
        self.assertRaises(zoo.InvalidSyntax,zoo.Elephant.presentation,"European")
