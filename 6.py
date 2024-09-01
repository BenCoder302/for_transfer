path = input("Enter the name of file to be read: ")

file = open(path, "r")
text = file.read()
words = text.split()

out = []
for word in words:
    word = word + '#'
    out.append(word)
final = "".join(out)
print(final)
file.close()
