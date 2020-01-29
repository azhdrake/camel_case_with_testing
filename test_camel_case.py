from unittest import TestCase
import camelCase

class TestCamelCase(TestCase):
    def test_camel_case_normal_input(self):
        sentence = 'This is a totally normal sentence.'
        expected_output = 'thisIsATotallyNormalSentence.'

        actual_output = camelCase.camel_case(sentence)

        self.assertEqual(actual_output, expected_output)

    def test_camel_case_gamzee_time(self):
        sentence = 'ThIs Is A tOtAlLy NoRmAl SeNtEnCe.'
        expected_output = 'thisIsATotallyNormalSentence.'

        actual_output = camelCase.camel_case(sentence)

        self.assertEqual(actual_output, expected_output)

    def test_camel_case_line_break(self):
        sentence = 'This is a totally \nnormal sentence.'
        expected_output = 'thisIsATotallyNormalSentence.'

        actual_output = camelCase.camel_case(sentence)

        self.assertEqual(actual_output, expected_output)

    def test_camel_case_tab_break(self):
        sentence = 'This is a totally \tnormal sentence.'
        expected_output = 'thisIsATotallyNormalSentence.'

        actual_output = camelCase.camel_case(sentence)

        self.assertEqual(actual_output, expected_output)

    def test_camel_case_emoji(self):
        sentence = '🔴 🟠 🟡 🟢 🔵 🟣 🟤 🟥 🟧 🟨 🟩 🟦 🟪 🟫.'
        expected_output = '🔴🟠🟡🟢🔵🟣🟤🟥🟧🟨🟩🟦🟪🟫.'

        actual_output = camelCase.camel_case(sentence)

        self.assertEqual(actual_output, expected_output)

    def test_camel_case_many_spaces(self):
        sentence = 'This  is   a  totally  normal   sentence.'
        expected_output = 'thisIsATotallyNormalSentence.'

        actual_output = camelCase.camel_case(sentence)

        self.assertEqual(actual_output, expected_output)

    def test_camel_case_starting_spaces(self):
        sentence = '        This is a totally normal sentence.'
        expected_output = 'thisIsATotallyNormalSentence.'

        actual_output = camelCase.camel_case(sentence)

        self.assertEqual(actual_output, expected_output)

    def test_camel_case_trailing_spaces(self):
        sentence = 'This is a totally normal sentence                        .'
        expected_output = 'thisIsATotallyNormalSentence.'

        actual_output = camelCase.camel_case(sentence)

        self.assertEqual(actual_output, expected_output)

    def test_camel_case_weird_characters(self):
        sentence = '        Th¤s is a tötall¥ normal ƒentence.'
        expected_output = 'th¤sIsATötall¥NormalƑentence.'

        #Apparently 'ƒ' has an upper case varient. Who knew? 

        actual_output = camelCase.camel_case(sentence)

        self.assertEqual(actual_output, expected_output)        