

market = {"A":10,"B":4,"C":7,"D":2} # Data Dict

o = {} # Empty Dict
for i in sorted(market.items(), key = lambda x:x[1]):
    # For loop
    # variable 'i' going through the sorted sequence of 
    # the itemed version of market dict, {"A":10, "B":5} --> [("A", 10), ("B":4)]
    # ie.   {"A":10, "B":4} --> [("A", 10), ("B":4)]
    # and simultanisouly sorting the NUMBERS 
    # [("A", 10), ("B":4)] --> [("B":4), ("A":10)]  #Ascending order...    
    
    #The key (Right side of items...   eg, A in {"A":10}, B in {"B":10}) being the value.
    o[i[0]] = i[1]
    # in simple terms, {X:Y} becomes {Y:X}

# The Element with smallest value.. with the value at INDEX 0, ie, starting place
print(list(o.items())[0][::-1])

# The Element with largest value... with the value at INDEX 0, ie, starting place
print(list(o.items())[-1][::-1])


# Printing the whole Dictionary as a list of tuples...
# {'D': 2, 'B': 4, 'C': 7, 'A': 10} --> [('D', 2), ('B', 4), ('C', 7), ('A', 10)]
print(list(o.items()))

