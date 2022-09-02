#pythaon program to return elem that are odd

def odd_in_list(g, x):
    c = []
    for i in g:
         if i % 2 == 1:
            c.append(i)
    return c

#driver code
#printing elements that are odd

if odd_in_list([1, 11, 7, 8, -1, 6], (11)) == [1, 11, 7, -1]:
    print("test passed")
else:
    print("test failed")

if odd_in_list([6, 8, 2], ()) == []:
    print("test passed")
else:
    print("test failed")