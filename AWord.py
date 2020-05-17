#https://codeforces.com/contest/59/problem/A

word = input()

lowerCaseCharsCount = sum(map(str.islower, word))  # =0
upperCaseCharsCount = sum(map(str.isupper, word))  # =0

# for ele in word:
#     if ele.islower():
#         lowerCaseCharsCount += 1
#     else:
#         upperCaseCharsCount += 1

if lowerCaseCharsCount >= upperCaseCharsCount:
    print(word.lower())
else:
    print(word.upper())
