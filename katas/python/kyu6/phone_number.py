# def create_phone_number(n):
#     """
#     1. take in an array of 10 integers 
#     2. Need to split the array into 3 sections and create a string 
#     3. error handling string must be 10 integers and only contain numbers 
#     """
#     if len(n) == 10 and all(isinstance(item, int) for item in n) :
#         area_code = ''.join(str(x) for x in n[:3])
#         exchange_code = ''.join(str(x) for x in n[3:6])
#         number = ''.join(str(x) for x in n[6:10])
        
#         full_number = f"({area_code}) {exchange_code}-{number}"
     
#     else :
#         return 'Number must be 10 digits'        
#     return full_number

# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

"""
Cleaner example
"""
def create_phone_number(n):
    if all(isinstance(item, int) for item in n):
        return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)  #* unpacks a list 
    else: 
        return "numbers must be integers"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))