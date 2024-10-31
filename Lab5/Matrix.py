# Реалізувати класи «Вектор» та «Матриця» (за потреби також клас «Система лінійних
# рівнянь»). У даному практикумі розглядаються виключно квадрати матриці, ви можете
# врахувати це в своїй реалізації. Класи повинні реалізовувати базові операції над матриця-
# ми (додавання, віднімання, множення матриць; множення матриці на вектор)

from copy import copy as cp, deepcopy as dcp


class Matrix:
    def __init__(self, matrix: list[list[float]]):
        self.matrix = matrix
        self.shape = (len(matrix), len(matrix[0]))

    @property
    def T(self) -> 'Matrix':
        return Matrix([[self.matrix[row][col] for row in range(self.shape[0])] for col in range(self.shape[1])])

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

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, index, value):
        self.matrix[index] = value

    def copy(self):
        return cp(self)

    def deepcopy(self):
        return dcp(self)

    def __str__(self):
        text = ''
        for row in self.matrix:
            text += str(row) + '\n'  # Print each row
        return text.strip()


if __name__ == '__main__':
    m1 = Matrix([[1, 2], [3, 4]])
    print("m1, m1.T", m1, m1.T, sep='\n')
    m1[0], m1[1] = m1[1], m1[0]
    m1[0][1] = 100
    print("m1, m1.T", m1, m1.T, sep='\n')
    m2 = Matrix([[1, 2], [3, 4]])
    m3 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
    m4 = Matrix([[1, 2, 3], [3, 4, 5]])
    m5 = Matrix([[1, 2], [3, 4], [5, 6]])
    v1 = Matrix([[1, 2]])
    v3 = Matrix([[2, 3]])
    v2 = Matrix([[1, 2, 3]])
    print("v1.T * v3", v1.T * v3, sep='\n')
    print("m1 * v1.T", m1 * v1.T, sep='\n')
    print("m3 * v2.T", m3 * v2.T, sep='\n')
    print("m1 + m2", m1 + m2, sep='\n')
    print("m1 - m2", m1 - m2, sep='\n')
    print("m1 * m2", m1 * m2, sep='\n')
    print("m1 * 2", m1 * 2, sep='\n')
    print("m4 * m5", m4 * m5, sep='\n')
