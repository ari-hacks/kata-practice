

# def reverse_number(n):
#     str_number = str(n)
#     if str_number.startswith("-"):
#         str_number = str_number[1:]
#         return -(int(str_number[::-1]))
#     else:
#      return int(str_number[::-1])


def reverse_number(n):
 if n < 0: return -reverse_number(-n) 
 return int(str(n)[::-1])


print(reverse_number(-123))