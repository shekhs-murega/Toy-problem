def exactly_two_positive(a, b, c):
    positive_count = 0
    
    # Check if each number is positive 
    # Then increment the count if so
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    # Return True if exactly two numbers are positive, otherwise False
    return positive_count == 2

# Get user input for numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Calculate the result by calling the function
result = exactly_two_positive(a, b, c)

# Display the result
print(f"Result: {result}")
