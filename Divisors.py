#create a program that prompts the user to enter a number
#and return all the numbers that are a divisor of that number
number = int(input("Enter a number: "))
x = [1,2,3,4,5,6,7,8,9]
div = []
for i in x:
    if number % i == 0:
        div.append(i)
print("The number you entered is divisible by: ", div)



