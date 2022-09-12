#python program to write a given string to a file
#and read file content and verify file contains only given string.
#return false if file is not created,or content do not match with string.

def lil(string):
    file1 = open("gpa.txt", "w")
    file1.write(string)
    file1 = open("gpa.txt", "r")
    G = file1.read()

    if string in G:
        print('Found In File')
    else:
	    print('Not Found In File')

    file1.close()
lil("how are you?")