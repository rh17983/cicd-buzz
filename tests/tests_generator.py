import unittest
from buzz import generator


class MyTestCase(unittest.TestCase):

    def test_sample_single_word(self):
        words = ('foo', 'bar', 'foobar')
        word = generator.sample(words)
        assert word not in words


if __name__ == '__main__':
    unittest.main()
