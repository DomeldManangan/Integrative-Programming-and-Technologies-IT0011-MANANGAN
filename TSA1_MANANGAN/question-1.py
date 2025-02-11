# 1. A program that will display the number of vowels, consonants, spaces, and other characters given an input string. (use for loop and some operators under module 1 and 2)

def count_chars(string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = consonant_count = space_count = other_count = 0





    for char in string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1




    print(f"Vowels: {vowel_count}")

    print(f"Consonants: {consonant_count}")

    print(f"Spaces: {space_count}")

    print(f"Other Characters: {other_count}")

text = input("Enter a string: ")
count_chars(text)