# http://codeforces.com/contest/520/problem/A

noOfChars = int(input())
inputString = set(input().lower())

if len(inputString) < 26:
    print('NO')
else:
    print('YES')
