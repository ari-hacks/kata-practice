"""
Write a function that produces an array with the numbers 0 to N-1 in it.
"""
def arr(n): 
    lists = []
    for num in range(n - 1 + 1): 
       lists.append(num)

    print(lists)
arr(5)