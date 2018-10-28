#write code to create a new list from given list containing only elements of given list
#that are less than or equal to 5
a = [1,1,2,3,5,8,13,21,34,55,89]
list = []
for i in a:
    if i not in list:
        if i <=5:
            list.append(i)
print(list)

        