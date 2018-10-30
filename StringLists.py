# ask user to input a word, then tell user whether or not the word is a palindrome
word = input("Please enter a word for palindrome testing: ")
letters_list = []
for letter in word:
    letters_list.append(letter)
reverse = letters_list[::-1]
if letters_list == reverse:
    print("Your word is a palindrome!")
else:
    print("Your word is not a palindrome. Try again.")


