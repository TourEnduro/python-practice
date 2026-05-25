directions = ['north', 'south', 'east', 'west', 'up', 'down']
verbs = ['go', 'kill', 'eat']
stops = ['the', 'in', 'of']
nouns = ['bear', 'princess']
numbers = ['3', '91234']
errors = ['AFJHASDKASD']

def scan(sentence):
    words = sentence.lower().split()
    result = []
    
    for word in words:
        if word in directions:
            result.append(('direction', word))
        elif word in verbs:
            result.append(('verb', word))
        elif word in stops:
            result.append(('stop', word))
        elif word in nouns:
            result.append(('noun', word))
        elif word.isdigit():
            result.append(('number', word))
        else:
            result.append(('error', word))

    return result