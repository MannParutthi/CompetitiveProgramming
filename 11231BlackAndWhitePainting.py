# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2172

while True:
    noOfRows, noOfCols, colorOfBottomRightCorner = [int(x) for x in input().split(' ')]
    if noOfRows == 0 and noOfCols == 0 and colorOfBottomRightCorner == 0:
        break
    else:
        ans = ((noOfRows-7) * (noOfCols-7) + colorOfBottomRightCorner) // 2
        print(ans)
