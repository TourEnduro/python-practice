from ex48 import lexicon

def test_direction():
    assert(lexicon.scan("north") == [('direction', 'north')])
    assert(lexicon.scan("north south east") == [
        ('direction', 'north'),
        ('direction', 'south'),
        ('direction', 'east')])
    
def test_verbs():
    assert(lexicon.scan("go") == [('verb', 'go')])
    assert(lexicon.scan("go kill eat") == [
        ('verb', 'go'),
        ('verb', 'kill'),
        ('verb', 'eat')])
    
def test_stops():
    assert(lexicon.scan("the") == [('stop', 'the')])
    assert(lexicon.scan("the in of") == [
        ('stop', 'the'),
        ('stop', 'in'),
        ('stop', 'of')])
    
def test_nouns():
    assert(lexicon.scan("bear") == [('noun', 'bear')])
    assert(lexicon.scan("bear princess") == [
        ('noun', 'bear'),
        ('noun', 'princess')])
    
def test_numbers():
    assert(lexicon.scan("1234") == [('number', '1234')])
    assert(lexicon.scan("3 91234") == [
        ('number', '3'),
        ('number', '91234')])
    
def test_errors():
    assert(lexicon.scan("afjhasdkasd") == [('error', 'afjhasdkasd')])
    assert(lexicon.scan("bear ias princess") == [
        ('noun', 'bear'),
        ('error', 'ias'),
        ('noun', 'princess')])