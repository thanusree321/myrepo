#python program to return no.of occurrance of a substring exists

def str_exist(g, f):
    p = len(f)
    count = 0
    for i in range(len(g) - len(f) + 1):
         if(g[i:i + len(f)] == f):
            count += 1
    return count

#driver code
#printing no.of occurance of a substring

if str_exist("abcdefmnacyxabchjmlabcjjjkh", ("abc")) == 3:
    print("test passed")
else:
    print("test failed")

if str_exist("abcdefmnacyxh", ("mnay")) == 0:
    print("test passed")
else:
    print("test failed")

