city=["Delhi","Mumbai","Chennai","Kolkata"]
print(city) #prints the whole list
print(city[0]) #accessing the first element of the list
print(city[1:3]) #slicing the list from index 1 to 2
print(city[-1:-4:-1]) #reversing a list using slicing
print(len(city)) #length of the list
city.append("Bangalore") #adding an element to the end of the list
print(city)
city[2] = "Hyderabad" #modifying an element in the list
print(city)
city.remove("Mumbai") #removing an element from the list
print(city)
city.pop() #removing the last element from the list
print(city)
city.insert(1,"Pune") #inserting an element at a specific index
print(city)
city.sort() #sorting the list in ascending order
print(city)
city.find("Delhi") #finding the index of a specific element in the list
city.count("Delhi") #counting the occurrences of a specific element in the list
city.clear() #removing all elements from the list

#tuple is like list but the difference is it is immutable