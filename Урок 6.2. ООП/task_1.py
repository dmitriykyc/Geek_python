class Matrix:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        for i in range(len(self.param)):
            for i_2 in range(len(other.param[i])):
                self.param[i][i_2] += other.param[i][i_2]
        return Matrix(self.param)


    def __str__(self):
        for i in self.param:
            for i_2 in range(len(i)):
                print('  ' + str(i[i_2]) + ' ', end= '')
            print('')
        return ''




matr_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matr_2 = Matrix([[10, 10], [10, 10], [10, 10]])
print(matr_1 + matr_2)
