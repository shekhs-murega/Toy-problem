# Toy-problem

## Code Challenge
This repository contains solutions to three coding challenges solved in Python. Each challenge has its own function and input/output method. Below are the details of each challenge:
### Challenge 1: Convert 12-Hour Time to 24-Hour Time

#### Description
The function convert_to_24hour(hour, minute, period) converts a 12-hour time (with 'am' or 'pm') to a four-digit string representing the time in 24-hour format.
##### Example
   ```bash
   result = convert_to_24hour(8, 30, "am")  # Output: "0830"

   ```
#### How it works
The convert_to_24hour function takes the hour, minute, and period as input. It checks if the time is 'am' or 'pm' and converts the 12-hour format to a four-digit 24-hour format. It handles cases where the hour needs to be adjusted based on the period.

### Challenge 2: Two numbers are positive

#### Description
The function exactly_two_positive(a, b, c) takes three integers as arguments and returns True if exactly two of the integers are positive numbers, and False otherwise.
##### Example 
   ```bash
   result = exactly_two_positive(2, 4, -3)  # Output: True

   ```
#### How it works
The function exactly_two_positive counts the number of positive integers among a, b, and c. If exactly two of them are positive, it returns True; otherwise, it returns False.

### Challenge 3: Consonant value

#### Description
The function solve(s) takes a lowercase string with no spaces and returns the highest value of consonant substrings. Consonants are any letters except 'aeiou'.
##### Example
   ```bash
result = solve("zodiacs")  # Output: 26

   ```
#### How it works
The solve function calculates the value of each consonant substring within the provided string. It disregards vowels ('aeiou') and assigns values based on their positions in the alphabet. Then, it finds the highest value among all the consonant substrings.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the appropriate challenge directory.
3. Run the Python script corresponding to the challenge (e.g., `conversion_time.py` for Challenge 1).
4. Follow the prompt to input the required data.
5. The script will display the output based on the input provided.

Feel free to explore the code for each challenge, modify it as needed, and experiment with different inputs.


## License
This project is licensed under the MIT License.

