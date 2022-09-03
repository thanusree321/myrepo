#python program to get no.of records that match given record
#in given list of persons.if not match,return 0

def gng(recs, findredc):
    cnt = 0
    for ele in recs:
        found = True
        for k in findredc:
            if k not in ele or findredc[k] != ele[k]:
                found = False
                break
        if found:
            cnt = cnt + 1
    print(cnt)

gng( [{"fname": "abc01", "lname": "xyz02", "age": "32",
         "address": "111 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "32",
         "address": "112 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "43",
         "address": "113 xyz rd, abc city, MD, 21774"},
        {"fname": "abc03", "lname": "xyz02", "age": "22",
         "address": "114 xyz rd, abc city, MD, 21774"}
        ]
, {"fname": "abc01", "lname": "xyz02"})


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


gng( [{"fname": "abc01", "lname": "xyz02", "age": "32",
         "address": "111 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "32",
         "address": "112 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "43",
         "address": "113 xyz rd, abc city, MD, 21774"},
        {"fname": "abc03", "lname": "xyz02", "age": "22",
         "address": "114 xyz rd, abc city, MD, 21774"}
        ]
, {"fname": "abc02", "lname": "xyz02","age":"43"})