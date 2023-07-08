import pytest
from left_join.left_join import left_join
from hash_table.hash_table import Hashtable

def test_left_join():
    hash1 = Hashtable()
    hash1.set('fond', 'enamored')
    hash1.set('wrath', 'anger')
    hash1.set('diligent', 'employed')
    hash1.set('outfit', 'garb')
    hash1.set('guide', 'usher')

    hash2 = Hashtable()
    hash2.set('fond', 'averse')
    hash2.set('wrath', 'delight')
    hash2.set('diligent', 'idle')
    hash2.set('guide', 'follow')
    hash2.set('flow', 'jam')

    actual = left_join(hash1, hash2)
    actual.sort()
    expected = [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['outfit', 'garb', None], ['guide', 'usher', 'follow']]
    expected.sort()
    assert actual == expected

def test_left_join2():
    hash1 = Hashtable()
    hash1.set('saif', 'obeidat')
    hash1.set('emam', 'mounqer')
    hash1.set('mohammed', 'shahin')
    

    hash2 = Hashtable()
    hash2.set('saif', 'mohammed')
    hash2.set('emam', 'mfedi')
    hash2.set('diligent', 'idle')
    
    actual = left_join(hash1, hash2)
    actual.sort()
    expected = [['saif', 'obeidat', 'mohammed'], ['emam', 'mounqer', 'mfedi'], ['mohammed', 'shahin', None]]
    expected.sort()
    assert actual == expected
    

def test_left_join_empty():
    hash1 = Hashtable()
    hash2 = Hashtable()
    actual = left_join(hash1, hash2)
    expected = []
    assert actual == expected