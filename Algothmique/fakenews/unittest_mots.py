import unittest
from mots import selection

class KnownValues(unittest.TestCase):

    known_values=(
        ("Donald Trump is the French President",
         ["Donald","Trump","French","President"]),
        
        ("Donald Trump is the US President.",
         ["Donald","Trump","US","President"]),

        ("Italy counts more than one million coronavirus cases.",
         ["Italy","counts","more","than","one","million","coronavirus","cases"]),

        ("France won the last World Cup.",
         ["France","won","last","World","Cup"]),

        ("Scientists consider that the earth is flat.",
         ["Scientists","earth","flat"]),

        ("Facebook is going to launch a new cryptomoney.",
         ["Facebook","launch","new","cryptomoney"]))


    def test_selection_mots(self):
        '''the phrase should give these important words'''

        for phrase, mots in self.known_values:
            result=selection(phrase)
            self.assertEqual(result,mots)

if __name__=='__main__':
    unittest.main()
    
        
        
