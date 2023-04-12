

output = [] # Empty List
for num in range(1,4): # Variable 'num' going through range of numbers 1-4, ie, 1,2,3
    # Variable i going through List of letters, ie [A, B, C]
    for l in ['A', 'B', 'C']:
        # Using F strings to place the letter at beginning and the number later, 
        # ie  A1, B1, C1
        string = f"{l}{num}"

        # Appending (adding) the variable 'string' to the output list
        output.append(string)

# Printing the list
print(output)
