#python program which returns true or false
#if substring exists

def str_exist():
    s = "abcdefmnacyxh"
    ss = "mnay"
    s1 = "abcdefmnacyxh"
    ss1 = "mna"

#driver code
#printing true or false if substring exists

    if ss in s:
        print("true")
    else:
        print("false")

    if ss1 in s1:
        print("true")
    else:
        print("false")
str_exist()