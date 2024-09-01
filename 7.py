# Display number of vowels, consonants, lowercase and uppercase letters in a file
file = open("test.txt", "r")
ch = ""
vowels = 0
consonants = 0
uppercase = 0
lowercase = 0

ch = file.read(1)
while ch:
    if ch == '\n':
        ch = file.read(1)
        continue
    if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        vowels += 1
    else:
        consonants += 1
    if ch.isupper():
        uppercase += 1
    if ch.islower():
        lowercase += 1
    ch = file.read(1)

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
file.close()
