# http://codeforces.com/contest/263/problem/A

matrix = []
noOfSwaps = 0

for i in range(0, 5):
    matrix.append(input().split(' '))

for i, row in enumerate(matrix):
    for j, ele in enumerate(row):
        if ele == '1':
            noOfSwaps = abs(i - 2) + abs(j - 2)
            print(noOfSwaps)
            break
