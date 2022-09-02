#python program to return elem that are odd.
#and less than or equal to given number

def less_or_equal_odd(g, x):
    c = []
    for i in g:
        if i <= x and i % 2 == 1:
            c.append(i)
    return len(c)

#driver code
#printing odd and lessThanOrEqual to given num

if less_or_equal_odd([1, 11, 7, 8, -1, 6], (11)) == 4:
    print("test passed")
else:
    print("test failed")

if less_or_equal_odd([1, 11, 7, 8, -1, 6], (18)) == 4:
    print("test1 passed")
else:
    print("test1 failed")

if less_or_equal_odd([1, 11, 7, 8, -1, 6], (-1)) == 1:
    print("test2 passed")
else:
    print("test2 failed")

if less_or_equal_odd([1, 11, 7, 8, -1, 6], (-2)) == 0:
    print("test3 passed")
else:
    print("test3 failed")