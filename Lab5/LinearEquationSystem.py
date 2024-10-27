# Реалізувати алгоритм LUP-розкладу матриці.

# Реалізувати алгоритм розв'язання системи ліні
# них рівнянь за допомогою LUP-розкладу

# Відкрити довільний підручник з лінійної алгебри і знайти там задачі, в яких вимагається
# розв'язати систему лінійних рівнянь розмірами пе менше 6 х 6 (бажано 10 х 10 або ще більше)

# Розв'язати знайдену систему за допомогою вашої реалізації.

# Перевірити знайдений розв'язок за допомогою системи WolframAlpha або аналогічної, якій
# ми довіряємо більше, ніж нашим реалізація.

from Matrix import Matrix


def lup_decomposition(matrix):
    pi = [i for i in range(matrix.shape[1])]  # columns
    l = Matrix([[0 for col in range(matrix.shape[1])] for row in range(matrix.shape[0])])
    u = Matrix([[0 for col in range(matrix.shape[1])] for row in range(matrix.shape[0])])
    p = Matrix([[0 for col in range(matrix.shape[1])] for row in range(matrix.shape[0])])
    for k in range(matrix.shape[0]):  # rows
        ks = -float("inf")
        for i in range(k, matrix.shape[0]):  # rows
            if ks < abs(matrix[i][k]):
                ks = abs(matrix[i][k])
                row_to_swap = i
        if matrix[row_to_swap][k] == 0:
            raise ValueError("Matrix is Invertible")
        if row_to_swap != k:
            pi[k], pi[row_to_swap] = pi[row_to_swap], pi[k]
            matrix[k], matrix[row_to_swap] = matrix[row_to_swap], matrix[k]
        for i in range(k + 1, matrix.shape[0]):  # rows
            matrix[i][k] /= matrix[k][k]
            for j in range(k + 1, matrix.shape[1]):  # columns
                matrix[i][j] -= matrix[i][k] * matrix[k][j]

    for row in range(matrix.shape[0]):  # Create l, u, p
        for col in range(matrix.shape[1]):
            if col == pi[row]:
                p[row][col] = 1
            if row <= col:
                if row == col:
                    l[row][col] = 1
                u[row][col] = matrix[row][col]
            else:
                l[row][col] = matrix[row][col]

    return l, u, p


class LinearEquationSystem:
    def __init__(self, matrix_of_equations: Matrix, b: Matrix):
        self.matrix = matrix_of_equations
        self.b = b

    def solve(self):
        l, u, p = lup_decomposition(self.matrix)
        bs = p * self.b
        y = Matrix([[0] for row in range(self.matrix.shape[0])])
        x = Matrix([[0] for row in range(self.matrix.shape[0])])
        for k in range(self.matrix.shape[0]):
            sum = 0
            for i in range(k):
                sum += l[k][i] * y[i][0]
            y[k] = [bs[k][0] - sum]
        for k in range(self.matrix.shape[0] - 1, -1, -1):
            sum = 0
            for i in range(k + 1, self.matrix.shape[0]):
                sum += u[k][i] * x[i][0]
            x[k] = [(y[k][0] - sum) / u[k][k]]
        return x


if __name__ == '__main__':
    m = Matrix([
        [1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6],
        [1, 3, 6, 10, 15, 21],
        [1, 4, 10, 20, 35, 56],
        [1, 5, 15, 35, 70, 126],
        [1, 6, 21, 56, 126, 252],
    ])
    m_copy = m.deepcopy()
    b = Matrix([
        [15],
        [35],
        [70],
        [126],
        [210],
        [336],
    ])
    les = LinearEquationSystem(m, b)
    x = les.solve()
    print()
    print("x.T: ", list(map(lambda x: round(x[0], 2), x)))
    print("\nCalculated b.T:", list(map(lambda x: round(x[0], 2), m_copy * x)), sep='\n')
    print("\nReal b.T:", b.T, sep='\n')
