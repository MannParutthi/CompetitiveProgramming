# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1393

noOfTests = int(input())
allowedAlphabets = 'IEHOVA#'

for i in range(noOfTests):
    rows, cols = [int(x) for x in input().split(' ')]
    matrix = []
    startPoint = []
    endPoint = []
    path = []
    for r in range(rows):
        matrix.append(list(input()))
    for rowNo, rowEle in enumerate(matrix):
        if '@' in rowEle:
            startPoint = [rowNo, rowEle.index('@')]
        if '#' in rowEle:
            endPoint = [rowNo, rowEle.index('#')]

    if startPoint[0] > endPoint[0]:
        nextStep = -1
    elif endPoint[0] > startPoint[0]:
        nextStep = 1
    else:
        nextStep = 0

    previousRow = startPoint[0]
    previousCol = startPoint[1]

    while True:
        if previousCol < endPoint[1]:
            if matrix[previousRow+nextStep][previousCol] in allowedAlphabets:
                previousRow += nextStep
                path.append('forth')
            elif previousCol+1 <= cols-1 and matrix[previousRow][previousCol+1] in allowedAlphabets:
                previousCol += 1
                path.append('right')
            elif previousCol-1 >= 0 and matrix[previousRow][previousCol-1] in allowedAlphabets:
                previousCol -= 1
                path.append('left')
            else:
                break
        else:
            if matrix[previousRow+nextStep][previousCol] in allowedAlphabets:
                previousRow += nextStep
                path.append('forth')
            elif previousCol-1 >= 0 and matrix[previousRow][previousCol-1] in allowedAlphabets:
                previousCol -= 1
                path.append('left')
            elif previousCol+1 <= cols-1 and matrix[previousRow][previousCol+1] in allowedAlphabets:
                previousCol += 1
                path.append('right')
            else:
                break

        if '#' == matrix[previousRow][previousCol]:
            break

    print(' '.join(path))
