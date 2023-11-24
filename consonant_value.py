def solve(s):
    # Define a dictionary to map letters to their corresponding values
    letter_values = {letter: ord(letter) - ord('a') + 1 for letter in 'abcdefghijklmnopqrstuvwxyz'}

    # Function to calculate the value of a substring
    def substring_value(sub):
        return sum(letter_values[char] for char in sub)

    vowels = 'aeiou'
    consonant_substrings = []

    # Split the string into consonant substrings
    current_substring = ''
    for char in s:
        if char.lower() not in vowels:
            current_substring += char
        else:
            if current_substring:
                consonant_substrings.append(current_substring)
                current_substring = ''

    if current_substring:
        consonant_substrings.append(current_substring)

    # Calculate the value for each consonant substring
    values = [substring_value(sub) for sub in consonant_substrings]

    # Return the highest value among consonant substrings
    return max(values, default=0)

# Get user input for the string
word = input("Enter a lowercase word with no spaces: ")

# Calculate and display the result
result = solve(word)
print(f"Highest value of consonant substrings: {result}")
