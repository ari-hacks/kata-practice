def is_isogram(string):
    string_to_list = list(string.lower())
  
    return False if len(string_to_list) != len(set(string_to_list)) else True

# print(is_isogram("mose"))