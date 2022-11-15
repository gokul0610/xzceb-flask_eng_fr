import unittest
import translator as tr

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(tr.english_to_french(' '),'Salut')
        self.assertEqual(tr.english_to_french('Hello'),'Bonjour')
        
        
class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(tr.french_to_english(' '),'How are you')
        self.assertEqual(tr.french_to_english('Bonjour'),'Hello')
        
unittest.main()