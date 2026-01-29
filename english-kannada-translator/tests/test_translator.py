import unittest
from translator.translator import translate

class TestTranslator(unittest.TestCase):

    def test_translation(self):
        self.assertEqual(translate("Hello"), "ಹಲೋ")
        self.assertEqual(translate("Goodbye"), "ಗೋಡ್‌ಬೈ")
        self.assertEqual(translate("Thank you"), "ಧನ್ಯವಾದಗಳು")
        self.assertEqual(translate("Yes"), "ಹೌದು")
        self.assertEqual(translate("No"), "ಇಲ್ಲ")

if __name__ == '__main__':
    unittest.main()