# http://codeforces.com/contest/766/problem/A

stringOne = input()
stringTwo = input()

if stringOne == stringTwo:
    print(-1)
else:
    print(max(len(stringOne), len(stringTwo)))
