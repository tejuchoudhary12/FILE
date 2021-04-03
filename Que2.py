my_file=open("text2.txt", "r")
a=0
c=my_file.read()
countList = c.split("\n")

for i in countList:
    if i :
        a +=1

print("The number of lines are:", a)
