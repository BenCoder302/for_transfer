# Copying particular line numbers
infile = input("Enter the source file name: ")
outfile = input("Enter the destination file name: ")
line_nos = eval(input("Enter the line numbers to copy as a list: "))

file = open(infile, "r")
lines = file.readlines()    # Stores lines as list
file.close()

file = open(outfile, "w")
for num in line_nos:
    file.write(lines[num - 1])
file.close()
