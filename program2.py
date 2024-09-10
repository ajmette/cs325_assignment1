num = input("Enter an integer: ")

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print("your number is even")
    elif num % 2 == 1:
        print("your number is odd")
else:
    print("integer was not entered")