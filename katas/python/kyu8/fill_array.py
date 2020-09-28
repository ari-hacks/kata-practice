"""
Write a function that produces an array with the numbers 0 to N-1 in it.
"""
def fill_array(n = ""): 
    lists = []
    if n:
        for num in range(n - 1 + 1): 
            lists.append(num)
        return lists
    elif n == 0: 
        return []
    else: 
        return []
        
        
