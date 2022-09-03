#python program which returns no.of occurrences
#of a char in string

def char(g, x):
    count = 0
    for i in g:
         if(i == x) :
               count = count+1
    return count

#driver code
#printing no.of occurrance of a char in string

if char("abcdefmnacyxh", ("a")) == 2:
    print("test passed")
else:
    print("test failed")