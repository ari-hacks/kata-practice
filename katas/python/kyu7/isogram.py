def is_isogram(string):
    return False if len(string.lower()) != len(set(string.lower())) else True
