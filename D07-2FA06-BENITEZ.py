# Version 2: Student Information Formatter

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

full_name = (first_name + " " + last_name).title()

print("\nFormatted Output:")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section.upper())
print("Favorite Subject:", favorite_subject.title())
print("Character Count:", len(full_name))