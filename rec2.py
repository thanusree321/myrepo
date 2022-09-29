#python program to return matching records.
#if no matching found,then return empty list

def gng(recs, findredc):
    f = []
    for item in recs:
        found = True
        for k in findredc:
            if item[k] != findredc[k]:
                found = False
                break
        if found == True:
            return item

    return None


allrecs =[{"fname": "abc01", "lname": "xyz02", "age": "32", "address": "111 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "32", "address": "112 xyz rd, abc city, MD, 21774"},
        {"fname": "abc03", "lname": "xyz02", "age": "43", "address": "113 xyz rd, abc city, MD, 21774"},
        {"fname": "abc03", "lname": "xyz02", "age": "22", "address": "114 xyz rd, abc city, MD, 21774"}
    ]
find = {"fname": "abc02", "lname": "xyz02", "age": "32"}
exp = {"fname": "abc02", "lname": "xyz02", "age": "32", "address": "112 xyz rd, abc city, MD, 21774"}

if gng(allrecs, find) == exp:
    print("test passed")
else:
    print("test failed")

allrecs =[{"fname": "abc01", "lname": "xyz02", "age": "32", "address": "111 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "32", "address": "112 xyz rd, abc city, MD, 21774"},
        {"fname": "abc03", "lname": "xyz02", "age": "43", "address": "113 xyz rd, abc city, MD, 21774"},
        {"fname": "abc03", "lname": "xyz02", "age": "22", "address": "114 xyz rd, abc city, MD, 21774"}
    ]
find = {}
exp ={"fname": "abc03", "lname": "xyz02", "age": "43", "address": "113 xyz rd, abc city, MD, 21774"}

if gng(allrecs, find) != exp:
    print("test passed")
else:
    print("test failed")