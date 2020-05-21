import score 
import unittest
from score import give_score,OutOfRangeError

### pour le test, changer quelques lignes dans la fonction give_score dans score.py, afin d'avoir comme paramètre de la fonction la phrase de l'utilisateur (enlever le input)

class KnownValues(unittest.TestCase):
    known_values = (
        (
            "France won the last World Cup",
            True
        ),
        (
            "Donald Trump becomes the US president",
            True
        ),
        (
            "Queen Elizabeth wants to abdicate",
            False
        ),
        
    )

    def test_score_known_values(self):
        """give_score should give known result with known input"""
        for phrase, known in self.known_values:
            if (give_score(phrase)>=50):
                etat=True
            else :
                etat=False
            self.assertEqual(known,etat)


class ScoreBadInput(unittest.TestCase):

    def test_is_empty(self):
        """give_score should fail with an empty input"""
        phrase=""
        self.assertRaises(OutOfRangeError, give_score, phrase)

    def test_number_words(self):
        """give_score should fail with a too short sentence"""
        phrase="Macron is"
        self.assertRaises(OutOfRangeError, give_score, phrase)
        
if __name__ == "__main__":
    unittest.main()
