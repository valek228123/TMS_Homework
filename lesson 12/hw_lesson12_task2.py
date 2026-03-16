class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        string_matrix = ""
        for row in self.matrix:
            string_matrix += str(row) + "\n"
        return string_matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            new_matrix = []
            for row in range(len(self.matrix)):
                list_row = []
                for col in range(len(self.matrix[row])):
                    list_row.append(self.matrix[row][col] + other.matrix[row][col])
                new_matrix.append(list_row)
            return Matrix(new_matrix)
        return NotImplemented

    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            new_matrix = []
            for row in range(len(self.matrix)):
                list_row = []
                for col in range(len(self.matrix[row])):
                    list_row.append(self.matrix[row][col] - other.matrix[row][col])
                new_matrix.append(list_row)
            return Matrix(new_matrix)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            new_matrix = []
            for row in range(len(self.matrix)):
                list_row = []
                for col in range(len(self.matrix[row])):
                    list_row.append(self.matrix[row][col] * other)
                new_matrix.append(list_row)
            return Matrix(new_matrix)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def transposition(self):
        new_matrix = []
        for col in range(len(self.matrix[0])):
            list_row = []
            for row in range(len(self.matrix)):
                list_row.append(self.matrix[row][col])
            new_matrix.append(list_row)
        return Matrix(new_matrix)

    @classmethod
    def creat_identity_matrix(cls, n: int, m: int):
        new_matrix = []
        for row in range(n):
            new_row = []
            for col in range(m):
                if row == col:
                    new_row.append(1)
                else:
                    new_row.append(0)
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    @classmethod
    def creat_zero_matrix(cls, n: int, m: int):
        new_matrix = []
        for row in range(n):
            new_row = []
            for col in range(m):
                new_row.append(0)
            new_matrix.append(new_row)
        return cls(new_matrix)

    @classmethod
    def creat_diagonal_matrix(cls, list1: list[int]):
        new_matrix = []
        len_matrix = len(list1)
        for row in range(len_matrix):
            new_row = []
            for col in range(len_matrix):
                if col == row:
                    new_row.append(list1[row])
                else:
                    new_row.append(0)
            new_matrix.append(new_row)
        return cls(new_matrix)

    @property
    def dimension_matrix(self):
        return (len(self.matrix), len(self.matrix[0]))

    @property
    def len_matrix(self):
        return len(self.matrix) * len(self.matrix[0])

    @property
    def sum_matrix(self):
        all_sum = 0
        for row in self.matrix:
            all_sum += sum(row)
        return all_sum

    def new_matrix_without_negative(self):
        new_matrix = []
        for row in self.matrix:
            new_row = []
            for col in row:
                if col >= 0:
                    new_row.append(col)
                else:
                    new_row.append(0)
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def __eq__(self, other):
        return self.matrix == other.matrix


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
c = Matrix([[1, -1, 1], [1, 1, -1], [-3, 3, 3]])
d = Matrix([[1, -1, 1], [1, 1, -1], [-3, 3, 3]])
list1 = [1, 2, 3, 4, 5, 6]
print(a)
print(a.transposition())
print(Matrix.creat_zero_matrix(3, 3))
print(Matrix.creat_diagonal_matrix(list1))
print(a.len_matrix)
print(c.new_matrix_without_negative())
print(a == b)
print(c == d)
