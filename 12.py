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

# __main__
choice = int(input("What do you want to do?\n1. Create\n2. Modify\nEnter your choice: "))
path = input("Enter the path of csv file: ")
if choice == 1:
    create(path)
elif choice == 2:
    modify(path)
