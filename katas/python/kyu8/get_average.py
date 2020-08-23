import math 
"""
Get the average of a list and round to low
"""
def get_average(marks):
    return math.floor(sum(marks)/len(marks))
