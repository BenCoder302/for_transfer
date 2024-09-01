# Copy and search records in binary file
import pickle

def write():
    f = open("Stu.dat", "wb")
    while True:
        r = int(input("Enter roll no.: "))
        n = input("Enter name: ")
        data = [r, n]
        pickle.dump(data, f)
        ch = input("More?(y/n) ")
        if ch in 'Nn':
            break
    f.close()

def search():
    found = 0
    rollno = int(input("Enter roll no. whose name you want to display: "))
    f = open("Stu.dat", "rb")
    try:
        while True:
            rec = pickle.load(f)
            if rec[0] == rollno:
                print(rec[1])
                found = 1
                break
    except EOFError:
        f.close()
    if found == 0:
        print("Sorry! No record found.")

# __main__
write()
search()
