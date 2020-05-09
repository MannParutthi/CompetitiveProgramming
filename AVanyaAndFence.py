# http://codeforces.com/contest/677/problem/A

fenceHeight = int(input().split(' ')[1])
friendsHeightList = input().split(' ')

widthOfRoad = 0

for ele in friendsHeightList:
    if int(ele) <= fenceHeight:
        widthOfRoad += 1
    else:
        widthOfRoad += 2

print(widthOfRoad)
