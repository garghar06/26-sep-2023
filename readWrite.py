file2=open("file2.txt",'w')

with open("file1.txt",'r') as scan:
    file2.write(scan.read())

file2.close()
