def find_missing(arr1, arr2):
    #convert each integer to string
    # diff = [str(number) for number in arr1 if number not in arr2 or arr2.remove(number)]
    # res = int("".join(diff))
    # return res
    return sum(arr1) - sum(arr2)

          

print(find_missing([1, 2, 2, 3], [1, 2, 3]))


