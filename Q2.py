
# List containing Multiple tuples of names and heights
details = [('John', 168), ('Joseph', 160), ('Arun', 178), ('Vishal', 172)] 

# using sorted function to sort the list.
# By default, sorted function sorts based off the first element in the sub data set, #ie, first element in every tuple.
# to sort based off the height, ie, the item at INDEX 1, ie at 2nd place
# we use key = lambda x: x[1]
# that means instead of checking by the first element/item, we check the 2nd item
print(sorted(details, key = lambda x: x[1]))



