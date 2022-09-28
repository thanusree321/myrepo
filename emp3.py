import json
with open('emp3.json', "r") as fd:
    jsondata = fd.read()
    re = json.loads(jsondata)

def gng(recs, findredc, replace):
    A = []
    for ele in recs:
        found = True
        for i in findredc:
            if i not in ele or findredc[i] != ele[i]:
                found = False
                break
        if found:
            A.append(ele)
            ele.update(replace)

    return exp

recs =[{"fname": "abc01", "lname": "xyz02", "age": "32",
         "address": "111 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "32",
         "address": "112 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "43",
         "address": "113 xyz rd, abc city, MD, 21774"},
        {"fname": "abc03", "lname": "xyz02", "age": "22",
         "address": "114 xyz rd, abc city, MD, 21774"}
        ]
find = {"fname": "abc02", "lname": "xyz02"}
replace = {"address": "214 xyz11 rd, abc11 city, MD, 21774"}
exp = {"fname": "abc02", "lname": "xyz02", "age": "43", "address": "214 xyz11 rd, abc11 city, MD, 21774"}

if gng(recs, find, replace) == exp:
    print("test passed")
else:
    print("test failed")


