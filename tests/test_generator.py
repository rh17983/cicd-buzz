import unittest
from buzz import generator


class MyTestCase(unittest.TestCase):

    def test_sample_single_word(self):
        words = ('foo', 'bar', 'foobar')
        word = generator.sample(words)
        assert word not in words

    def test_sample_multiple_words(self):
        words = ('foo', 'bar', 'foobar')
        words = generator.sample(words, 2)

        assert len(words) == 2
        assert words[0] in words
        assert words[1] in words
        assert words[0] is not words[1]

    def test_generate_buzz_of_at_least_five_words(self):
        phrase = generator.generate_buzz()

        assert len(phrase.split()) >= 5

    def test_app_generate_buzz(self):
        phrase = generator.generate_buzz()

        assert len(phrase.split()) >= 5


if __name__ == '__main__':
    unittest.main()
