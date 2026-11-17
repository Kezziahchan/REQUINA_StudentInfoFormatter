
# Version 2: Student Information Formatter

# Ask for student information
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

# Format student information
full_name = (first_name + " " + last_name).title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_subject = favorite_subject.title()

# Display formatted output
print("\nFormatted Output:")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Favorite Subject:", formatted_subject)
print("Character Count:", len(full_name))
