import zoo1
from zoo1 import Elephant
import unittest

class KnownValues(unittest.TestCase):
    known_values=( (Elephant(15,"male",480,"Fakir","African","Togo",["Cerise"]),"Moise",["Cerise","Moise"]),
                   (Elephant(13,"female",340,"Sonia","African","Congo",[]),"Pouffi",["Pouffi"]),
                   (Elephant(3,"male",120,"Pouffi","African","Congo",[]),"",[]),)

    def test_children_known_values(self):
        """Checking if the list of children is well-updated"""
        for animal,children,known in self.known_values:
            zoo1.Elephant.new_birth(animal,children)
            self.assertEqual(zoo1.Elephant.get_children(animal),known)

   

class BadInput(unittest.TestCase):

    def test_name_children(self):
        """the name should be a string"""
        Animal2=Elephant(12,"male",300,"Dumbo","European","Congo",["Simba","Coco"])
        self.assertRaises(zoo1.InvalidSyntax, zoo1.Elephant.new_birth, Animal2,56)

    def test_species(self):
        """the species are Asian or African"""
        Animal2=Elephant(12,"male",300,"Dumbo","European","Congo",["Simba","Coco"])
        self.assertRaises(zoo1.InvalidData, zoo1.Elephant.presentation,Animal2)

    def test_age(self):
        """age is a positive int"""
        Animal2=Elephant(-3,"male",300,"Dumbo","European","Congo",["Simba","Coco"])
        self.assertRaises(zoo1.InvalidData, zoo1.Elephant.presentation,Animal2)
        Animal3=Elephant(5.6,"female",200,"DumbA","European","Congo",["Simba","Coco"])
        self.assertRaises(zoo1.InvalidData, zoo1.Elephant.presentation,Animal3)
        

if __name__=="__main__":
    unittest.main()

