# http://codeforces.com/contest/768/problem/A

noOfStewards = int(input())
strengthOfEachStewards = [int(x) for x in input().split(' ')]

noOfStewardsJonSnowWillSupport = 0
minStrength = min(strengthOfEachStewards)
maxStrength = max(strengthOfEachStewards)

for strength in strengthOfEachStewards:
    if minStrength < strength < maxStrength:
        noOfStewardsJonSnowWillSupport += 1

print(noOfStewardsJonSnowWillSupport)
