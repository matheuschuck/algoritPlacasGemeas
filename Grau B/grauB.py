def solve(n, matrix, i):
    soma = -1
    if(i>=n):
        return -1
    elif(sum(matrix[0]) == sum(matrix[1])):
        #print(sum(matrix[0]))
        soma = sum(matrix[0])
    temp0 = matrix[0][i]
    temp1 = matrix[1][i]
    soma0 = solve(n, matrix, i+1)
    matrix[0][i] = temp1
    matrix[1][i] = temp0
    soma1 = solve(n, matrix, i+1)
    #print(matrix, " ",i)
    return max(soma0, soma1, soma)

def solveB(n, mat, z):
    mat2= mat.copy()
    mat2[0] = mat[0].copy()
    mat2[1] = mat[1].copy()
    mat2[0][z] = 0
    mat2[1][z] = 0
    return solve(n, mat2, 0)

def algoritm(mm):
    r = solve(3, mm, 0)
    mZ = -1
    if(r==-1):
        for z in range(0,len(mm[0])):
            #print(mm)
            tempR = solveB(len(mm),mm,z)
            if(tempR>r):
                r = tempR
                mZ = z
            elif(tempR==r):
                if(min(mm[0][z], mm[1][z]) <= min(mm[0][mZ], mm[1][mZ])):
                    mZ = z
                    
    if(r==-1):
        print("impossível")
    elif(mZ==-1):
        print(r,"nenhuma placa descartada")
    else:
        print(r,"descartada a placa",mm[0][mZ],mm[1][mZ])
        
        
    


mm = [[10,10,10],[10,11,10]]
algoritm(mm)
#print(mm)
#print(sum(mm[0]))



