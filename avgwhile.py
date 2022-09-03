#python program to return average of all elem in list.
#using while loop

def avg_ele(g):
    p = len(g)
    i = 0
    s = 0
    while i < p:
        s = s + g[i]
        i = i + 1
    c = s/p
    return round(c, 2)

#driver code
#printing average of all elem

if avg_ele([1, 11, 7, 8, -1, 6, 3]) == 5:
    print("test passed")
else:
    print("test failed")

if avg_ele([1, 11, 17, 28, -1, 6]) == 10.33:
    print("test1 passed")
else:
    print("test1 failed")