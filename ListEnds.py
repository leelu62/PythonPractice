#Write a program that takes a list of elements
#and creates a new list, using a function, that contains only the 
#first and last elements of the first list
list1 = [2,4,5,8,9,1]
def newlist(list):
    return [list[0],list[-1]]
print(newlist(list1))




