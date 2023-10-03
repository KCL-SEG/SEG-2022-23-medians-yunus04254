"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [int(value) for value in input().split(",")]
        numbers.sort()

        numlen = len(numbers)
        if len(numbers) % 2 == 1:
            median = numbers[numlen // 2]
        else:
            m1 = numbers[(numlen // 2)-1]
            m2 = numbers[(numlen // 2)]
            median = (m1 + m2) /2

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(float(median))