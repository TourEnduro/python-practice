import pytest
from ex49.parser import *

def test_parser():
    x = parse_sentence([('verb', 'run'), ('direction', 'north')])
    
    assert x.subject == 'player'
    assert x.verb == 'run'
    assert x.object == 'north'

    y = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])

    assert y.subject == 'bear'
    assert y.verb == 'eat'
    assert y.object == 'honey'

def test_errors():
    with pytest.raises(ParserError):
        parse_sentence([('direction', 'north')])