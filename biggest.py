# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    if len(list_of_numbers) ==0:
        return 0
    elif len(list_of_numbers) ==1:
        return listof_numbers
    else:
        i = 1
        bigger = list_of_numbers[0]
        while i+1 <= len(list_of_numbers):
            if bigger <= list_of_numbers[i]:
                bigger = list_of_numbers[i]
            else:
                bigger = bigger
            i = i +1
    return bigger



print greatest([4,23,1])
#>>> 23
#print greatest([])
#>>> 0
