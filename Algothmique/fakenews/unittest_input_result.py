import score 
import unittest
from score import give_score, OutOfRangeError

class KnownValues(unittest.TestCase):
    known_values = (
        (
            "US counts more than one milion coronavirus cases",
            40
        ),
        (
            "France won the last World Cup",
            65
        ),
        (
            "Donald Trump is the US president",
            52
        ),
        
    )

    def test_score_known_values(self):
        """give_score should give known result with known input"""
        for phrase, known in self.known_values:
            self.assertEqual(known, give_score(phrase))


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
