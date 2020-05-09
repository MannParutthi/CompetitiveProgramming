# http://codeforces.com/contest/791/problem/A

weightsList = input().split(' ')

limarksWeight = int(weightsList[0])
bobsWeight = int(weightsList[1])
noOfYears = 0

while limarksWeight <= bobsWeight:
    noOfYears += 1
    limarksWeight = 3 * limarksWeight
    bobsWeight = 2 * bobsWeight

print(noOfYears)