import zoo
from zoo import Giraffe
import unittest

class KnownValues(unittest.TestCase):
    known_values = ( (Giraffe(13,"female",120,5.2,70,4.0),10,80),
                     (Giraffe(13,"female",120,5.2,70,4.0),30,100),
                     (Giraffe(13,"female",120,5.2,10,4.0),10,20),
                     (Giraffe(13,"female",120,5.2,42,4.0),50,92),
                     (Giraffe(13,"female",120,5.2,1,4.0),26,27) )

    def test_add_food_known_values(self):
        '''add_food should give known result with known input'''
        for inp_1,inp_2, known in self.known_values:
            result = zoo.Giraffe.add_food(inp_1,inp_2) 
            self.assertEqual(known, result)

class ZooBadInput(unittest.TestCase):
    
    def test_negative(self):
        '''get_height should fail with negative input'''
        Animal1=Giraffe(13,"female",120,-1,70,4.0)
        self.assertRaises(zoo.OutOfRangeError, zoo.Giraffe.get_height, Animal1)

    def test_valuefood1(self):
        '''get_daily_check should fail with negative self.food'''
        Animal1=Giraffe(13,"female",120,5.2,-1,4.0)
        self.assertRaises(zoo.OutOfRangeError, zoo.Giraffe.get_daily_check, Animal1)

    def test_valuefood2(self):
        '''get_daily_check should fail with self.food > 100'''
        Animal1=Giraffe(13,"female",120,5.2,101,4.0)
        self.assertRaises(zoo.OutOfRangeError, zoo.Giraffe.get_daily_check, Animal1)


if __name__=="__main__":
    unittest.main()

