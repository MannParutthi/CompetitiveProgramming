# https://codeforces.com/contest/770/problem/A

lengthOfPassword, noOfDistinctSymbols = [int(x) for x in input().split(' ')]

password = ''
possibleChars = ' abcdefghijklmnopqrstuvwxyz'  # It starts from 1 so ' ' in added in the start
noOfDistinctSymbolsInPassword = 0

for i in range(lengthOfPassword):
    if noOfDistinctSymbolsInPassword < noOfDistinctSymbols:
        noOfDistinctSymbolsInPassword += 1
        password += possibleChars[noOfDistinctSymbolsInPassword]
    else:
        if noOfDistinctSymbols % 2 == 0:
            if i % 2 == 0:
                password += possibleChars[noOfDistinctSymbolsInPassword - 1]
            else:
                password += possibleChars[noOfDistinctSymbolsInPassword]
        else:
            if i % 2 == 0:
                password += possibleChars[noOfDistinctSymbolsInPassword]
            else:
                password += possibleChars[noOfDistinctSymbolsInPassword-1]

print(password)
