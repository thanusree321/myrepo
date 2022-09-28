import json
with open('empi.json', "r") as fd:
    jsondata = fd.read()
    re = json.loads(jsondata)

def gng(recs,findredc):
    cnt = 0
    for ele in recs:
        found = True
        for k in findredc:
            if k not in ele or findredc[k] != ele[k]:
                found = False
                break
        if found:
            cnt = cnt + 1

    return cnt

recs =[{"fname": "abc01", "lname": "xyz02", "age": "32",
         "address": "111 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "32",
         "address": "112 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "43",
         "address": "113 xyz rd, abc city, MD, 21774"},
        {"fname": "abc03", "lname": "xyz02", "age": "22",
         "address": "114 xyz rd, abc city, MD, 21774"}
        ]
find = {"fname": "abc01", "lname": "xyz02"}

if gng(recs, find) == 1:
    print("test passed")
else:
    print("test failed")

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

if gng(recs, find) == 2:
    print("test passed")
else:
    print("test failed")

recs =[{"fname": "abc01", "lname": "xyz02", "age": "32",
         "address": "111 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "32",
         "address": "112 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "43",
         "address": "113 xyz rd, abc city, MD, 21774"},
        {"fname": "abc03", "lname": "xyz02", "age": "22",
         "address": "114 xyz rd, abc city, MD, 21774"}
        ]
find = {"fname": "abc02", "lname": "xyz02", "age": "43"}

if gng(recs, find) == 1:
    print("test passed")
else:
    print("test failed")