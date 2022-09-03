#python program to return matching records.
#if no matching found,then return empty list

def gng(recs, findredc):
    A = []
    for ele in recs:
        found = True
        for k in findredc:
            if k not in ele or findredc[k] != ele[k]:
                found = False
                break
        if found:
           A.append(ele)
    print(A)

gng( [{"fname": "abc01", "lname": "xyz02", "age": "32",
         "address": "111 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "32",
         "address": "112 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "43",
         "address": "113 xyz rd, abc city, MD, 21774"},
        {"fname": "abc03", "lname": "xyz02", "age": "22",
         "address": "114 xyz rd, abc city, MD, 21774"}
        ]
, {"fname": "abc02", "lname": "xyz02"})