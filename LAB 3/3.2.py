# 3.2
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

full_name = f"{first_name} {last_name}"

full_name_upper = full_name.upper()
full_name_lower = full_name.lower()

full_name_length = len(full_name)

print(f"\nFull Name: {full_name}")
print(f"Full Name (Upper Case): {full_name_upper}")
print(f"Full Name (Lower Case): {full_name_lower}")
print(f"Length of Full Name: {full_name_length}")