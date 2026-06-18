word1="kush"
word2="Bhardwaj"
print(word1 + " " + word2) #concatenation of two strings
print(word1*3) #repetition of a string
print(word1[0]) #accessing the first character of the string
print(word1[1:4]) #slicing the string from index 1 to 3
print(len(word1)) #length of the string
print(word1.upper()) #converting the string to uppercase
print(word1.lower()) #converting the string to lowercase
print(word1.capitalize()) #capitalizing the first letter of the string  
print(word1.replace("k","K")) #replacing a character in the string
print(word1.split("h")) #splitting the string based on a character  
print(word1.strip()) #removing leading and trailing whitespace from the string
print(word1.startswith("k")) #checking if the string starts with a specific character
print(word1.endswith("j")) #checking if the string ends with a specific character
print(word1.find("h")) #finding the index of a specific character in the string
print(word1.count("h")) #counting the occurrences of a specific character in the string
print(word1.isalpha()) #checking if the string contains only alphabetic characters
print(word1.isdigit()) #checking if the string contains only digits 
print(word1.isalnum()) #checking if the string contains only alphanumeric characters
print(word1.islower()) #checking if the string is in lowercase
print(word1.isupper()) #checking if the string is in uppercase
print(word1.isspace()) #checking if the string contains only whitespace characters
print(word2[-1:-5:-1]) #reversing a string using slicing
print(word2[::-1]) #reversing a string using slicing with step -1
print(word2[-3:-1]) #slicing the string 