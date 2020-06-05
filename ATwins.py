# http://codeforces.com/contest/160/problem/A

noOfCoins = int(input())
valueOfEachCoin = sorted([int(x) for x in input().split(' ')], reverse=True)

for index in range(noOfCoins):
    if sum(valueOfEachCoin[0:index+1]) > sum(valueOfEachCoin[index+1:]):
        print(index+1)
        break
