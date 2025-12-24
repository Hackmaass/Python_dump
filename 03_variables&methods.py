#Variables and methods in Python

quote = "Everything's faire in love and war."

print(quote) # prints the quote variable

#methods
print(quote.upper())  # converts the string to uppercase

print(quote.lower())  # converts the string to lowercase

print(quote.title())  # converts the string to title case

print(len(quote))  # gets the length of the string


name - "Omkar" #string variable
age = 21 #integer variable
gpa = 3.8 #float variable

print('My name is ' + name + ', I am ' + str(age) + ' years old and my GPA is ' + str(gpa) + '.') #concatenation of strings and variables

age += 1 #incrementing age by 1
print('Next year, I will be ' + str(age) + ' years old.') #printing the incremented age

birthday = 1
age += birthday #adding birthday to age
print('After my birthday, I will be ' + str(age) + ' years old.') #printing the incremented age