#write a python program of multilevel inheritance
class Animal:
    def eat(self):
        print("Eating...") 

class Dog(Animal):
    def bark(self):
        print("Barking...")
        

class Puppy(Dog):
    def weep(self):
        print("Weeping...")
        
puppy = Puppy()
puppy.eat()  # Inherited from Animal class      
puppy.bark() # Inherited from Dog class
puppy.weep() # Defined in Puppy class   