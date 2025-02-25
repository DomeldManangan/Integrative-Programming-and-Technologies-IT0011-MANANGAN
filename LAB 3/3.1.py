# 3.1
first_name = input("What's your first name? ").strip()
last_name = input("And your last name? ").strip()
age = input("How old are you? ").strip()

full_name = f"{first_name} {last_name}"

nickname = first_name[:4] if len(first_name) >= 4 else first_name

greeting_message = f"Hey, {nickname}! Nice to meet you. You’re {age} years young!"

print(f"\nYour full name: {full_name}")
print(f"Here's a short and friendly name for you: {nickname}")
print(greeting_message)