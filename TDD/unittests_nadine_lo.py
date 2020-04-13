import unittest

from TDD.zoo1 import Elephant, InvalidData, InvalidSyntax


class KnownValues(unittest.TestCase):
    known_values = (
        (
            Elephant(15, "male", 480, "Fakir", "African", "Togo", ["Cerise"]),
            "Moise",
            ["Cerise", "Moise"]
        ),
        (
            Elephant(13, "female", 340, "Sonia", "African", "Congo", []),
            "Pouffi",
            ["Pouffi"]
        ),
        (
            Elephant(3, "male", 120, "Pouffi", "African", "Congo", []),
            "",
            []
        )
    )

    def test_children_known_values(self):
        """Checking if the list of children is well-updated"""
        for elephant, children, known in self.known_values:
            elephant.new_birth(children)
            self.assertEqual(elephant.children, known)


class BadInput(unittest.TestCase):

    def test_name_children(self):
        """the name should be a string"""
        elephant = Elephant(12, "male", 300, "Dumbo", "European", "Congo", ["Simba", "Coco"])
        self.assertRaises(InvalidSyntax, elephant.new_birth, 56)

    def test_species(self):
        """the species are Asian or African"""
        elephant = Elephant(12, "male", 300, "Dumbo", "European", "Congo", ["Simba", "Coco"])
        self.assertRaises(InvalidData, elephant.presentation)

    def test_age(self):
        """age is a positive int"""
        elephant = Elephant(-3, "male", 300, "Dumbo", "European", "Congo", ["Simba", "Coco"])
        self.assertRaises(InvalidData, Elephant.presentation, elephant)
        elephant = Elephant(5.6, "female", 200, "DumbA", "European", "Congo", ["Simba", "Coco"])
        self.assertRaises(InvalidData, elephant.presentation)


if __name__ == "__main__":
    unittest.main()
