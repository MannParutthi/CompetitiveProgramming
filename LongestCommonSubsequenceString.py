# https://www.youtube.com/watch?v=sSno9rV8Rhg

#1st Approach
def lcs(s1, s2):
    matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + s1[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)

    lcsStr = matrix[-1][-1] # OR lcsStr = matrix[len(s1)-1][len(s2)-1]
    print('Length of LCS:',len(lcsStr))
    print('LCS String:', lcsStr)

lcs('SHINCHAN', 'NOHARAAA') 


#2nd Approach
def LCS(X, Y):
    m = len(X) 
    n = len(Y)
    L = [[None]*(n + 1) for i in range(m + 1)]
    
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    print('Length of LCS:',L[m][n])
    
    i = m
    j = n
    lcsStr = ''
    while i > 0 and j > 0:
      if X[i-1] == Y[j-1]:
        lcsStr += X[i-1]
        i-=1
        j-=1
      elif L[i-1][j] > L[i][j-1]:
        i-=1
      else:
        j-=1
    print('LCS String:', lcsStr[::-1])
        
LCS('SHINCHAN', 'NOHARAAA')
