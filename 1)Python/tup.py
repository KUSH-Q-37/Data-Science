# Get tuple input from user
user_input = input("Enter integers separated by spaces: ")
numbers = tuple(map(int, user_input.split()))

# Create tuple of even numbers
even_nums = ()
for num in numbers:
    if num % 2 == 0:
        even_nums = even_nums + (num,)

# Create tuple of odd numbers
odd_nums = ()
for num in numbers:
    if num % 2 != 0:
        odd_nums = odd_nums + (num,)

print(f"Original tuple: {numbers}")
print(f"Even numbers: {even_nums}")
print(f"Odd numbers: {odd_nums}")