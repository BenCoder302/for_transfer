# Create and modify records
import pickle

t = {}
stufile = open("Stu.dat", "ab")
ans = "y"
while ans == "y":
    rno = int(input("Enter roll no.: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    t["rollno"] = rno
    t["name"] = name
    t["marks"] = marks

    pickle.dump(t, stufile)
    ans = input("Want to append more records?(y/n) ")

stufile.close()
