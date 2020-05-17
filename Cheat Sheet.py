# For taking input with space separated values and converting them into list of integers
StringValuesList = input().split(' ')  # 1 2 3 4
print(StringValuesList)
IntegerValuesList = [int(x) for x in input().split(' ')]  # 1 2 3 4
print(IntegerValuesList)


#  For taking input as string and converting it into list of integers
listOfStringInteger = [int(x) for x in list(input())]  # 1234321
print(listOfStringInteger)


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


# To Count no of Upper case and Lower case characters in a word
word = 'maTRIx'
lowerCaseCharsCount = sum(map(str.islower, word))
upperCaseCharsCount = sum(map(str.isupper, word))
print(lowerCaseCharsCount, upperCaseCharsCount)


# Dictionary Initialization and For loop on a dictionary
listOfInts = [6, 7, 8, 7, 6]
dictOfIntCounts = {}

for val in listOfInts:
    dictOfIntCounts[val] = listOfInts.count(val)
print(dictOfIntCounts)

for key, value in dictOfIntCounts.items():
    print(key, value)

