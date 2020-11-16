from cipher_kl3045 import __version__
from cipher_kl3045 import cipher_kl3045
import pytest

def test_version():
    assert __version__ == '0.1.4'

def test_sentence_with_spaces():
    result = cipher_kl3045.cipher('Bob hit the prince', 1)
    expected = 'Cpc iju uif qsjodf' #expected result, should the test pass
    assert result == expected