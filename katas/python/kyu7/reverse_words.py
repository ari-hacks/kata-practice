def reverse_words(text):
    return ' '.join([words[::-1] for words in text.split(' ')])

    
print(reverse_words("this is a string"))