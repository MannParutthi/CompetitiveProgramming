import math
from datetime import date

# For taking input with space separated values and converting them into list of integers
StringValuesList = input().split(' ')  # 1 2 3 4
print(StringValuesList)
IntegerValuesList = [int(x) for x in input().split(' ')]  # 1 2 3 4
print(IntegerValuesList)

#  For taking input as string and converting it into list of integers
listOfStringInteger = [int(x) for x in list(input())]  # 1234321
print(listOfStringInteger)

# For taking 2 or more inputs in space separated string
n1, n2 = [int(x) for x in input().split(' ')]  # 1 2
print(n1, n2)

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

# To find if value is an integer
val1 = 1.0
val2 = 1.43535
print(val1.is_integer(), val2.is_integer())

# Find minimum and maximum length of dictionary values which are in list format
dict1 = {1: [3, 4, 5], 2: [6, 7], 3: [8]}
print(min([len(x) for x in dict1.values()]), max([len(x) for x in dict1.values()]))

# To check if value is a perfect square - Perfect squares have odd number of factors
val1 = 2500
val2 = 2550
print(int(math.sqrt(val1)) ** 2 == val1)
print(int(math.sqrt(val2)) ** 2 == val2)

# To check if two dates are consecutive
if date(2020, 5, 22).toordinal() - date(2020, 5, 21).toordinal() == 1:
    print('Consecutive')
else:
    print('Non Consecutive')

# To make a dictionary from 1 to n with [] as value
# print({k+1: [] for k in range(3)})

#Sorting a list of objects by age and if age is same then by name
my_list = [
  {"name": "Smit", "age": 20 },
  {"name": "Jay", "age": 15 },
  {"name": "Jay", "age": 20 },
]
my_list.sort( key = lambda x: (x["age"], x["name"]) )
print(my_list)

#Substrings
s = "manan"
allPossibleSubstrings = [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
print(allPossibleSubstrings)

# Bubble Sort
def bubbleSort(a):
    noOfSwaps = 0
    swaped = False
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                noOfSwaps += 1
                swaped = True
        if swaped:
            swaped = False
        else:
            break
    return {noOfSwaps, a}

#bisect - for maintaining a list in sorted order without having to sort the list after each insertion (uses Array bisection algorithm)
import bisect
arr = [0,1,1,2] #array should be sorted
print(bisect.bisect_left(arr, 1)) #1 returns index of left most ele 
print(bisect.bisect_right(arr, 1)) #3 returns next index of right most ele
array = [0,2,3] #array should be sorted
bisect.insort(array, 1) #inserts value at the perfect position in sorted array  
print(array) #[0, 1, 2, 3]
