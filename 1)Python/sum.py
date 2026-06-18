a=5
b=3
sum = a + b
print("I Love {}".format("Python"))  #normal formatting
print("the sum of {} and {} is {}".format(a,b,sum)) #positional formatting
print("the sum of {1} and {0} is {2}".format(a,b,sum)) #positional formatting with index
print("the value of {c} and {d}".format(c=20,d=50)) #value formatting with keyword arguments
print(f"the sum of {a} and {b} is {sum}") #f-string formatting