# Dictionary to store student names and marks
students = {}

while True:
    print("\n--- Student Marks Management ---")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")
    
    choice = input("\nEnter your choice (A/B/C/D/E): ").upper()
    
    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print(f"Student '{name}' added successfully!")
    
    elif choice == 'B':
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print(f"Marks updated for '{name}'!")
        else:
            print(f"Student '{name}' not found!")
    
    elif choice == 'C':
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name}: {students[name]} marks")
        else:
            print(f"Student '{name}' not found!")
    
    elif choice == 'D':
        if students:
            print("\n--- All Students ---")
            for name, marks in students.items():
                print(f"{name}: {marks} marks")
        else:
            print("No students in the dictionary!")
    
    elif choice == 'E':
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice! Please enter A, B, C, D, or E.")