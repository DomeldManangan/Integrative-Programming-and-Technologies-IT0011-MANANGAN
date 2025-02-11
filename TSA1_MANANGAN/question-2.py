# A program that will count the sum of the digits from a given input string digits. (use for loop and some operators under module 1 and 2)

def sum_of_digits(string):
    total = 0

    for char in string:
        if char.isdigit():
            total += int(char)

    print(f"Sum of digits: {total}")

text = input("Enter a string with digits: ")
sum_of_digits(text)