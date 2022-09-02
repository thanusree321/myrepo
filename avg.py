#python function which returns the average of all elements in the list.
#if the list does not contain any elements,than return 0

def avg_ele(g):
    p = len(g)
    s = 0
    for i in g:
        s = s + i
    c = s/p
    return round(c, 2)

#driver code
#printing average of all elements
if (avg_ele([1, 11, 17, 28, -1, 6])) == 10.33:
    print("test passed")
else:
    print("test failed")
if (avg_ele([1, 11, 7, 8, -1, 6, 3])) == 5:
    print("test1 passed")
else:
    print("test1 failed")