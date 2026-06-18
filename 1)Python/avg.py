#Input two lists of integers from the user. Merge them into one list and sort the result
list1= int(input("Enter the number of elements in the list: "))
my_list = []
for i in range(list1):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)
list2 = int(input("Enter the number of elements in the second list: "))
my_list2 = []
for i in range(list2):
    element = int(input(f"Enter element {i+1}: "))
    my_list2.append(element)
list3 = my_list + my_list2
list3.sort()
print("Merged and sorted list:", list3)