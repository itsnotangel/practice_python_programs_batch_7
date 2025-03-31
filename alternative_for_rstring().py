# Program 1: Remove trailing spaces without using rstrip()

# Get input from the user
statement = input("Enter a statement: ")

# Initialize index to the last character of the string
index = len(statement) - 1

# Loop to find the last non-space character
while index >= 0 and statement[index] == ' ':
    index -= 1

# Extract the substring without trailing spaces
trimmed_statement = statement[:index + 1]

# Print the result
print("Trimmed statement: '" + trimmed_statement + "'")    