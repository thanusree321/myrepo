#python program which return max elem in a list

def largest(g):
    p = len(g)
    x = 0
    y = 0
    while y != len(g):
        if x < g[y]:
            x = g[y]
        y += 1
    return x

#driver code
#printing max element in list

if largest([1, 11, 17, 28, -1, 6]) == 28:
    print("test passed")
else:
    print("test failed")

if largest([1, 11, 8, -1, 6, 7]) == 11:
    print("test1 passed")
else:
    print("test1 failed")