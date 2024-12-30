# Create and modify csv file
import csv

def create(path):
    f = open(path, "w")
    csv_w = csv.writer(f)
    while True:
        data = eval(input("Enter data in row: "))
        csv_w.writerow(data)
        ch = input("Do you want to enter more data?(y/n) ")
        if ch == 'n':
            break
    f.close()

def modify(path):
    f = open(path, "a")
    csv_w = csv.writer(f)
    while True:
        data = eval(input("Enter data in row: "))
        csv_w.writerow(data)
        ch = input("Do you want to append more data?(y/n) ")
        if ch == 'n':
            break
    f.close()


def search(path):
    found = 0
    name = input("Enter name of student: ")
    try:
        f = open(path, "r")
        csv_r = csv.reader(f)
        for rec in csv_r:
            if rec[1] == name:
                print(f"Marks of {name} is {rec[2]}.")
                found = 1
                break
        f.close()
    except FileNotFoundError:
        print("File not found!")
    if found == 0:
        print("Sorry! No record found.")

# __main__
choice = int(input("What do you want to do?\n1. Create\n2. Modify\n3. Search\nEnter your choice: "))
path = input("Enter the path of csv file: ")
if choice == 1:
    create(path)
elif choice == 2:
    modify(path)
elif choice == 3:
    search(path)
else:
    print("Invalid choice!")
