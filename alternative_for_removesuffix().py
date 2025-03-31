# Program 2: Remove suffix without using removesuffix()

# Get input from the user
statement = input("Enter a statement: ")

# Assigned suffix to be removed
suffix = "ment"

# Check if the text ends with the suffix and remove it manually
if statement.endswith(suffix):
    statement = statement[:len(statement) - len(suffix)]

# Print the result
print(statement)