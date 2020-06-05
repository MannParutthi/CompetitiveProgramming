# https://codeforces.com/contest/71/problem/A

noOfWords = int(input())

for i in range(noOfWords):
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word)-2) + word[-1])
    else:
        print(word)
