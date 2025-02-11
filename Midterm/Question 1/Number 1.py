import os

def is_palindrome(num):
    """Check if a number is a palindrome."""
    return str(num) == str(num)[::-1]

def process_file(filename):
    """Process the file and check each line for palindrome sums."""
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    for index, line in enumerate(lines):




        stripped_line = line.strip()
        if not stripped_line:
            continue
        


        # Split the line into numbers
        numbers = stripped_line.split(',')




        # Convert strings to integers
        int_numbers = [int(num) for num in numbers if num.strip()]



        # Calculate the sum
        total_sum = sum(int_numbers)



        palindrome_status = "Palindrome" if is_palindrome(total_sum) else "Not a palindrome"

        
        # Print the result
        print(f"Line {index + 1}: {stripped_line} (sum {total_sum}) - {palindrome_status}")



# Call the function with the relative path to the file
process_file('./numbers.txt')