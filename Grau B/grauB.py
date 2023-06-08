import csv
import time

'''

Implementação da solução por força bruta para o problema
proposto de placas de jogos antigos.

Desenvolvido por Matheus Milanezi e Pedro Tubino

'''


# Inicio da contagem de tempo de execução
start = time.time()


def readPlates(file_path):
    # Método que lê as entradas em um arquivo .txt

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        n = int(next(reader)[0])
        matrix = [[], []]
        for row in reader:
            row = [int(num) for num in row]
            # Condição para ler várias instancias
            if len(row) == 1:
                algoritm(matrix, n)
                matrix = [[], []]
                end = time.time()
                total = end - start
                total = '%.4f' % total
                print(f'Tempo parcial: {total}')
                # n = int(next(reader))
            # print(row, "row")
            else:
                matrix[0].append(row[0])
                matrix[1].append(row[1])
            # print(matrix)

        # return matrix, n
        end = time.time()
        total = end - start
        total = '%.4f' % total  # saída setada para 4 números depois da vírgula
        return f"Fim: Tempo de execução total: {total} segundos."


def solve(n, matrix, i, again):
    '''
    Método que realiza a checagem sem excluir nenhuma peça.
    Apenas virando as peças.
    '''
    soma = -1
    if (i >= n):
        return -1
    elif ((again != 1) and (sum(matrix[0]) == sum(matrix[1]))):
        # print(sum(matrix[0]))
        soma = sum(matrix[0])
    temp0 = matrix[0][i]
    temp1 = matrix[1][i]
    soma0 = solve(n, matrix, i+1, 1)
    matrix[0][i] = temp1
    matrix[1][i] = temp0
    soma1 = solve(n, matrix, i+1, 0)
    # print(matrix, " ",i)
    return max(soma0, soma1, soma)


def solveB(n, mat, z):
    '''
    Método que faz a exclusão de uma peça e
    chama solve para somar o array com a peça removido.
    '''
    mat2 = mat.copy()
    mat2[0] = mat[0].copy()
    mat2[1] = mat[1].copy()
    mat2[0][z] = 0
    mat2[1][z] = 0
    return solve(n, mat2, 0, 0)


def algoritm(mm, n):
    '''
    Método principal.
    '''
    r = solve(n, mm, 0, 0)  # variável que salva a maior soma
    # Coordenada da placa que foi descartada // -1 = a nenhuma descartada
    mZ = -1
    if (r == -1):
        for z in range(0, n):
            # print(mm)
            tempR = solveB(len(mm), mm, z)
            if (tempR > r):
                r = tempR
                mZ = z
            elif (tempR == r):
                if (min(mm[0][z], mm[1][z]) <= min(mm[0][mZ], mm[1][mZ])):
                    mZ = z

    if (r == -1):
        print("impossível")
    elif (mZ == -1):
        print(r, "nenhuma placa descartada.")
    else:
        print(r, "descartada a placa", mm[0][mZ], mm[1][mZ])


# mm = [[10, 10, 10], [10, 11, 10]]
# algoritm(mm)
# print(mm)
# print(sum(mm[0]))
# file_path = './implementacao/Grau B/in_out/in1'
file_path = './in_out/in7'
# plates, n = readPlates(file_path)
print(readPlates(file_path))
# print(plates)
# algoritm(plates)
