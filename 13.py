"""
Stack Implementation
"""

def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False

def Push(stk, item):
    global top
    stk.append(item)
    top = len(stk) - 1

def Pop(stk):
    global top
    if isEmpty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1
        return item

def Peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top = len(stk) - 1
        return stk[top]

def Display(stk):
    if isEmpty(stk):
        print("Empty Stack")
    else:
        top = len(stk) - 1
        print(stk[top], "<- top")
        for i in range(top - 1, -1, -1):
            print(stk[i])

# __main__
stack = []
top = None
while True:
    print("\nStack Operations: ")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display stack")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        item = int(input("Enter a value: "))
        Push(stack, item)

    elif ch == 2:
        item = Pop(stack)
        if item == "Underflow":
            print("Underflow! Stack is empty!")
        else:
            print("Popped item:", item, end="")
            input()

    elif ch == 3:
        item = Peek(stack)
        if item == "Underflow":
            print("Underflow! Stack is empty!")
        else:
            print("Topmost item:", item, end="")
            input()

    elif ch == 4:
        Display(stack)

    elif ch == 5:
        break

    else:
        print("Invalid choice")
        input()
