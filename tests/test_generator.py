import unittest

from buzz import generator


def test_sample_single_word():
    words = ('foo', 'bar', 'foobar')
    word = generator.sample(words)
    assert word in words


def test_sample_multiple_words():
    words = ('foo', 'bar', 'foobar')
    words = generator.sample(words, 2)

    assert len(words) == 2
    assert words[0] in words
    assert words[1] in words
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()

    assert len(phrase.split()) >= 5
