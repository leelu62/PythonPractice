# prompt user to enter a number and return msg stating whether number is odd or even
number = int(input("Enter a number: "))
mod = number % 2
if mod > 0:
    print("The number you entered is odd.")
else:
    print("The number you entered is even.")

