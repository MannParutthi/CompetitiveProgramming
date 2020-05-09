# For taking input with space separated values and converting them into list of integers
StringValuesList = input().split(' ')
print(StringValuesList)
IntegerValuesList = [int(x) for x in input().split(' ')]
print(IntegerValuesList)

# To count the number of occurrences
lst = [8, 6, 8]
print(lst.count(8))

# Convert a list of integers into space separated string
print(' '.join([str(x) for x in lst]))

# Sorted List
print(sorted(lst))

# For loop with index
for index, value in enumerate(lst):
    print(index, value)

# Abstract value
print(abs(-1), abs(1))

# Unique Characters in a String
string = 'abcddbca'
uniqueCharacters = ''.join(set(string))
print(string, uniqueCharacters, len(uniqueCharacters))
