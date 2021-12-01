def swap():
    file1 = input("pls enter name of file1")
    file2 = input("pls enter name of file2")
    with open(file1,'r') as f1:
        inf1 = f1.read()
    with open(file2, 'r') as f2:
        inf2 = f2.read()
    with open(file1,'w') as f1:
        f1.write(inf2)
    with open(file2,'w') as f2:
        f2.write(inf1)
        
swap()