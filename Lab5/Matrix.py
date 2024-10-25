# Реалізувати класи «Вектор» та «Матриця» (за потреби також клас «Система лінійних
# рівнянь»). У даному практикумі розглядаються виключно квадрати матриці, ви можете
# врахувати це в своїй реалізації. Класи повинні реалізовувати базові операції над матриця-
# ми (додавання, віднімання, множення матриць; множення матриці на вектор)

# Реалізувати алгоритм LUP-розкладу матриці.

# Реалізувати алгоритм розв'язання системи ліні
# них рівнянь за допомогою LUP-розкладу

# Відкрити довільний підр:
# учник з лінійної алгебри і знайти там задачі, в яких вимагається
# розв'язати систему
# лінійних рівнянь розмірами пе менше 6 х 6 (бажано 10 х 10 або ще
# більше)

# Розв'язати знайдену систему за допомогою вашої реалізації.

# Перевірити знайдений розв'язок за допомогою системи WolframAlpha або аналогічної, якій
# ми довіряємо більше, ніж нашим реалізація.


class Matrix:
    def __init__(self, matrix: list[list[float]], T: 'Matrix' = None):
        self.matrix = matrix
        self.shape = (len(matrix), len(matrix[0]))
        if T is None:
            self.T = Matrix([[self.matrix[col][row] for col in range(self.shape[0])] for row in range(self.shape[1])], self)
        else:
            self.T = T

    def __add__(self, other: 'Matrix'):
        if other.__class__ != self.__class__:
            raise TypeError(f"Matrices must be of the {self.__class__.__name__} class, received {self.__class__.__name__} and {other.__class__.__name__}")
        if self.shape != other.shape:
            raise ValueError(f"Matrices must have the same shape, received {self.shape} and {other.shape}")
        return Matrix([[self.matrix[row][col] + other.matrix[row][col] for col in range(self.shape[1])] for row in range(self.shape[0])])

    def __sub__(self, other: 'Matrix'):
        if other.__class__ != self.__class__:
            raise TypeError(f"Matrices must be of the {self.__class__.__name__} class, received {self.__class__.__name__} and {other.__class__.__name__}")
        if self.shape != other.shape:
            raise ValueError(f"Matrices must have the same shape, received {self.shape} and {other.shape}")
        return Matrix([[self.matrix[row][col] - other.matrix[row][col] for col in range(self.shape[1])] for row in range(self.shape[0])])

    def __mul__(self, other: 'Matrix'):
        if other.__class__ != self.__class__:
            if other.__class__ != int:
                raise TypeError(f"Matrices must be of the {self.__class__.__name__} or int class, received {self.__class__.__name__} and {other.__class__.__name__}")
            else:
                return Matrix([[self.matrix[row][col] * other for col in range(self.shape[1])] for row in range(self.shape[0])])
        if self.shape != other.shape and self.shape[1] != other.shape[0]:
            raise ValueError(f"Matrices must have compatible shapes, received {self.shape} and {other.shape}")
        return Matrix([[sum(self.matrix[row][i] * other.matrix[i][col] for i in range(self.shape[1])) for col in range(other.shape[1])] for row in range(self.shape[0])])

    def __str__(self):
        text = ''
        for row in self.matrix:
            text += str(row) + '\n'  # Print each row
        return text  # .strip()


if __name__ == '__main__':
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2], [3, 4]])
    m3 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
    m4 = Matrix([[1, 2, 3], [3, 4, 5]])
    m5 = Matrix([[1, 2], [3, 4], [5, 6]])
    v1 = Matrix([[1, 2]])
    v2 = Matrix([[1, 2, 3]])
    print(m1 * v1.T)
    print(m3 * v2.T)
    print(m1 + m2)
    print(m1 - m2)
    print(m1 * m2)
    print(m1 * 2)
    print(m4 * m5)
