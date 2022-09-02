def avg_three_num(n1, n2, n3):
    return round((n1 + n2 + n3)/3, 2)

#cover exact division with 3
if avg_three_num(5, 5, 5) == 5:
    print("Test1: Pass")
else:
    print("Test1: Fail")

#cover rounding 3rd decimal value as <5
t2data = avg_three_num(-10, 20, 30)
if t2data == 13.33:
    print("Test2: Pass")
else:
    print("Test2: Fail")

#cover rounding 3rd decimal value as >5
t3data = avg_three_num(5, 6, 6)
if t3data == 5.67:
    print("Test3: Pass")
else:
    print("Test3: Fail")

#cover rounding 3rd decimal value as 5
t4data = avg_three_num(6, 3, 0.34655)
if t4data == 3.12:
    print("Tes4: Pass")
else:
    print("Test4: Fail")