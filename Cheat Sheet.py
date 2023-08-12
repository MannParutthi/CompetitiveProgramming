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
bubbleSort([5,4,1,2,3])

#bisect - for maintaining a list in sorted order without having to sort the list after each insertion (uses Array bisection algorithm)
import bisect
arr = [0,1,1,2] #array should be sorted
print(bisect.bisect_left(arr, 1)) #1 returns index of left most ele 
print(bisect.bisect_right(arr, 1)) #3 returns next index of right most ele
array = [0,2,3] #array should be sorted
bisect.insort(array, 1) #inserts value at the perfect position in sorted array  
print(array) #[0, 1, 2, 3]

# Merge Sort
def merge(a1, a2):
    swaps, i, j, result, m, n = 0, 0, 0, [], len(a1), len(a2)
    while i < m and j < n:
        if a1[i] <= a2[j]:
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1         # i => index of a1, m => length of a1
            swaps += m - i # arr is sorted so all ele after a1[i] along with it will be greater than a2[j] so a2[j] will be swapped will all those elements => thus (m-i) swaps
    result += a1[i:]
    result += a2[j:]    
    return swaps, result    
def msort(arr):
    n = len(arr)
    mid = n // 2
    if n > 1:
        left_swaps, left_result = msort(arr[:mid])
        right_swaps, right_result = msort(arr[mid:])
        m_swaps, result = merge(left_result, right_result)
        return m_swaps + left_swaps + right_swaps, result
    return 0, arr
msort([5,4,1,2,3])


# Counter - Gives the count of each element in dictionary format & can be accessed like a dictionary => for key, val in Counter(a).items()
from collections import Counter
a = "cde"
b = "abc"
print(Counter(a)) #Counter({'c': 1, 'd': 1, 'e': 1})
print(Counter(b)) #Counter({'a': 1, 'b': 1, 'c': 1})
print(Counter(a) & Counter(b)) #Intersection - Counter({'c': 1})
print(Counter(a) | Counter(b)) #Union - Counter({'c': 1, 'd': 1, 'e': 1, 'a': 1, 'b': 1})

# Optimal Way to find Prime Number
def isPrime(n) : 
  if (n <= 1) :  # 1 and no's less than 1 are not prime 
    return False
  if (n <= 3) : # 2 and 3 are prime numbers
    return True
  if (n % 2 == 0 or n % 3 == 0) : # any no divisible by 2 or 3 is not prime
    return False
 
  i = 5
  while(i * i <= n) : # factors after i*i<=n are same as before
    if (n % i == 0 or n % (i + 2) == 0) : # checking for i and i+2
      return False
    i += 6 #all the prime no's are of the form 6k+1 / 6k-1 (2 and 3 exception)
  return True

print(isPrime(997))

# Python Specifics
import collections
q = collections.deque()
q.append(1)
q.append(2) 
q.popleft() # 1 => pops first ele FIFO
q.pop() # 2 => pops last ele X 

# another way of queue
que = [1,2]
que.pop(0) # 1 => pops first ele FIFO
que.pop() # 2 => pops last ele X

dict = collections.defaultdict(list) # default dict ; all the values with ve initialized as [] empty list by default
dict['A'].append['B'] # => A: [B] => no need to initialize like if 'A' not in dict then dict['A'] = [] and then append

minHeap = []
heapq.heappush(minHeap, 1) # adds ele into heap
heapq.heappush(minHeap, 2) # adds ele into heap
heapq.heappush(minHeap, 3) # adds ele into heap
heapq.heappop(minHeap) # pops the min ele from heap => 1

# can be used inside a function - very useful for recursive funciton calls like DFS 
nonlocal q, que, dict, minHeap # so that there is no need to pass them in every func call

# Defining a positive infinite integer
positive_infinity = float('inf')
print('Positive Infinity: ', positive_infinity)
 
# Defining a negative infinite integer
negative_infinity = float('-inf')
print('Negative Infinity: ', negative_infinity)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposedMatrix = list(zip(*matrix)) # gives list of tuples
print("transposedMatrix => ", transposedMatrix) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

arr = [1,2,3,4,5,6,7,8]
print("Random Choice with equal probability", random.choice(arr)) # O(logn) / O(n)

print(random.randint(3, 9)) # Return a number between 3 and 9 (both inclusive)

print(random.random()) # returns a random number from 0.0 to 1.0

print("XOR of two similar values is always Zero", 2^2)

print("returns True if all items in an iterable are true, otherwise it returns False", all([True, True, True]), all([0, 1, 1]), all((0, True, False)) )

# get K largest elements & K smallest elements
freqMap = { 'A': 3, 'B': 4, 'C': 5, 'D': 1, 'E': 2, 'F': 3 }
k = 3 # if tie between two A & F has same freq => first occuring in freqMap
print(heapq.nlargest(k, freqMap.keys(), key=freqMap.get)) # ['C', 'B', 'A'] => 3 most freq ele
print(heapq.nsmallest(k, freqMap.keys(), key=freqMap.get)) # ['D', 'E', 'A'] => 3 least freq ele
