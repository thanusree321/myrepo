#python program to return max elem in a list

def highest(g):
    c = 0
    for i in g:
        if i > c:
            c = i
    return c

#driver code
#printing max element in given list

if highest([1, 11, 17, 28, -1, 6]) == 28:
    print("test passed")
else:
    print("test failed")

if highest([1, 11, 7, 8, -1, 6]) == 11:
    print("test1 passed")
else:
    print("test1 failed")