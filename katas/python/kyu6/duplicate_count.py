from collections import Counter
"""
Return the count of distinct case-insensitive alphabetic characters and numbers with duplicates
"""
def duplicate_count(text):
    dict_text = {}
    for key,val in Counter(text.upper()).items():
        if val > 1 : 
            dict_text[key] = val
    return len(dict_text)
 
    

print(duplicate_count("aA11"))