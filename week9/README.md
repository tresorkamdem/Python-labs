# Week 9 – Object-Oriented Programming (Advanced)

Author: Kamdem  
Course: Python Labs  
Topic: Inheritance, Composition, and OS Module  

------------------------------------------------------------
Lab Task 1: School Management System
------------------------------------------------------------

Concepts:
- Inheritance
- Method overriding
- Use of super()

Description:
This task implements a base class `Person` and two child classes:
- `Student`
- `Teacher`

Both inherit from `Person` and override the `introduce()` method.

Key Features:
- Base class with shared attributes (name, age)
- Student adds student_id
- Teacher adds subject
- Overridden introduce() methods
- Demonstration of polymorphism

Example Output:
Hi, I'm Alice, a student. My ID is S001 and I'm 16 years old.
Hello, I'm Mr. Smith, a teacher. I teach Mathematics and I'm 35 years old.

------------------------------------------------------------
Lab Task 2: Library System (Composition)
------------------------------------------------------------

Concepts:
- Composition ("has-a" relationship)
- Object containment
- List management
- Search functionality

Description:
A `Library` class contains multiple `Book` objects.

Key Features:
- Add books
- Remove books
- List books
- Search books by title
- Clear formatted outputs

Composition Relationship:
Library HAS Books

Example Output:
Added: Python Crash Course by Eric Matthes
Removed: Clean Code by Robert Martin
Found 1 book(s):
Python Crash Course by Eric Matthes

------------------------------------------------------------
Lab Task 3: File Manager with os Module
------------------------------------------------------------

Concepts:
- os module
- Directory handling
- File creation
- File renaming
- Cleanup operations

Operations Performed:
1. Display current working directory
2. Create folder "lab_files"
3. Create three text files
4. List files
5. Rename one file
6. Delete all files and folder

Important Functions Used:
- os.getcwd()
- os.mkdir()
- os.listdir()
- os.rename()
- os.remove()
- os.rmdir()
- os.path.exists()
- os.path.join()

All operations complete without errors and cleanup is performed at the end.

------------------------------------------------------------
Key Learning Outcomes
------------------------------------------------------------

✓ Understanding inheritance and method overriding  
✓ Understanding composition vs inheritance  
✓ Managing collections of objects  
✓ Practical use of Python's os module  
✓ Safe file handling and cleanup  

------------------------------------------------------------
End of Week 9
------------------------------------------------------------