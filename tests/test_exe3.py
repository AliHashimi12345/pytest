import pytest

def vowels():
     return set('aeiou')

@pytest.mark.skip
def test_vowels():
     result =  vowels()
     expected = set('aeiou')
     print ("this test has run")
     assert result == expected
