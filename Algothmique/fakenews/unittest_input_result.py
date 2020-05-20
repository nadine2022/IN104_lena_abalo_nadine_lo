import score 
import unittest
from score import scores, OutOfRangeError

class KnownValues(unittest.TestCase):
    known_values = (
        (
            "The Olympic Games in Tokyo has been postponed",
            49.275
        ),
        (
            "Scientists believe that the earth is flat",
            6.5
        ),
        (
            "Donald Trump is taking somme chloroquine",
            85.975
        ),
        
    )

    def test_score_known_values(self):
        """score should give known result with known input"""
        for phrase, known in self.known_values:
            self.assertEqual(known, scores(phrase))


class ScoreBadInput(unittest.TestCase):

    def test_is_empty(self):
        """score should fail with an empty input"""
        phrase=""
        self.assertRaises(OutOfRangeError, scores, phrase)

    def test_number_words(self):
        """score should fail with a too short sentence"""
        phrase="Macron is"
        self.assertRaises(OutOfRangeError, scores, phrase)
        
 if __name__ == "__main__":
    unittest.main()
