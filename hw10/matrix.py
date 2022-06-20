class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.matrix]) + '\n'

    def __add__(self, other):
        rezult = []
        if not isinstance(other, Matrix):
            raise ValueError('Only Matrix can be added')
        if len(self.matrix) != len(other.matrix):
            raise ValueError('Operands must have the same size')
        for row1, row2 in zip(self.matrix, other.matrix):
            if len(row1) != len(row2):
                raise ValueError('Operands must have the same size')
            rezult_row = [cell1 + cell2 for cell1, cell2 in zip(row1, row2)]
            rezult.append(rezult_row)
        return Matrix(rezult)


my_matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_matrix1)

my_matrix2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(my_matrix2)

sum_matrix = my_matrix1 + my_matrix2
print(sum_matrix)
