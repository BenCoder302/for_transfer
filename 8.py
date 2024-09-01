# First Letter capital
n = input("Enter a string: ")
a = n.split() 
b = []
c = ''
for i in a:
    if i[0].isalpha():
        if ord(i[0]) in range(65, 91): # Uppercase letters -> 65 to 90
            b.append(i)
        elif ord(i[0]) in range(97, 123): # Lowercase letters -> 97 to 122
            j = ''
            j += chr(ord(i[0]) - 32) + i[1::]
            b.append(j)
        else:
            b.append(i)
        b.append(' ')
    c = "".join(b)
print("Sentence with words having first letter capital:", c)
