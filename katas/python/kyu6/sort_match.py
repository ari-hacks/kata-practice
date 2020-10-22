#TODO make more performant 
def scramble(s1, s2):
    scrambled_word = set(s1)

    for letter in s2:
        if letter not in scrambled_word:
            return False
    return True

print(scramble('scriptingjava', 'javascript'))