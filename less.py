#python program to return no.of ele that are
#less than or equal to given number

def lessThanOrEqual(g, x):
    c = []
    for i in g:
        if i <= x:
            c.append(i)
    return len(c)

#driver code
#printing lessThanOrEqual to given num

if lessThanOrEqual([1, 11, 7, 8, -1, 6], (11)) == 6:
    print("test passed")
else:
    print("test failed")

if lessThanOrEqual([1, 11, 7, 8, -1, 6], (10)) == 5:
    print("test1 passed")
else:
    print("test1 failed")

if lessThanOrEqual([1, 11, 7, 8, -1, 6], (-1)) == 1:
    print("test2 passed")
else:
    print("test2 failed")

if lessThanOrEqual([1, 11, 7, 8, -1, 6], (-2)) == 0:
    print("test3 passed")
else:
    print("test3 failed")