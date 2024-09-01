# Menu-driven program for factorial and sum of numbers of a list

done = False

def factorial(n):
    temp = 1
    for i in range(1, n + 1):
        temp = temp * i
    return temp

def sum_of_list(my_list):
    sum = 0
    for i in range(0, len(my_list)):
        sum += int(my_list[i])
    return sum

def menu():
    print("\nWhat do you want to do?")
    print("1) Factorial of a number")
    print("2) Sum of numbers of a list")
    print("3) Quit\n")
    return int(input("Enter your choice: "))

def process():
    global done
    if(choice not in [1, 2, 3]):
        print("Invalid choice!", end="")
        input()     # For a pause
        return
    if(choice == 1):
        n = int(input("\nEnter a number: "))
        print(f"{n}! = {factorial(n)}", end="")
        input()     # For a pause
    if(choice == 2):
        my_list = eval(input("Enter a list of numbers: "))
        print(f"Sum of numbers of {my_list} = {sum_of_list(my_list)}", end="")
        input()     # For a pause
    if (choice == 3):
        done = True
        print("Quitting...")
        return

if __name__ == "__main__":
    while not done:
        choice = menu()
        process()
