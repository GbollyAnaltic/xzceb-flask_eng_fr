from translator import englishtofrench,frenchtoenglish

import unittest



class testenfr(unittest.TestCase):

    def test_eng_fr(self):

        self.assertEqual(englishtofrench('Hello'),'Bonjour')

        self.assertEqual(englishtofrench('My Love'),'Mon amour')

        self.assertEqual(englishtofrench(''),'Empty')

        self.assertNotEqual(englishtofrench('School'),'Lecole')



class testfren(unittest.TestCase):

    def test_fr_eng(self):

        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')

        self.assertEqual(frenchtoenglish('Mon amour'),'My Love')

        self.assertEqual(frenchtoenglish(''),'Empty')

        self.assertNotEqual(frenchtoenglish('Fleur'),'Flow')



unittest.main()