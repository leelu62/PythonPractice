#store family and friend's birthdays in a dictionary
#write a program that looks up the birthday of the person inputted by the user
birthdays_dict = {"Amon":"10/03/2016","Christopher":"12/18/1983","Jenna":"6/2/1985"}
person = input("Whose birthday would you like to look up? ")
print(person + "'s birthday is",birthdays_dict[person])


