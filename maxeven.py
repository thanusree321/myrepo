#python program to return max even element in the list

def highest_even(g):
    highest = 0
    for i in g:
        if i > highest and i % 2 == 0 :
            highest = i
    return highest

#driver code
#printing max even element

if highest_even([1, 11, 7, 8, -1, 6]) == 8:
    print("test passed")
else:
    print("test failed")

if highest_even([1, 11, 17, 28, -1, 6]) == 28:
    print("test passed")
else:
    print("test failed")