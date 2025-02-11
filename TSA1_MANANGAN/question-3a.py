# A program that will display the following given output. (for a. use nested for statement and for b. use nested while statement)

def pattern_a(rows=5):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "".join(str(num) for num in range(1, i + 1)))

pattern_a()