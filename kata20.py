class Sudoku(object):  # проверка правильно ли заполнена судоку
    def __init__(self, data):
        self.rows = []
        self.columns = []
        self.little_squares = []
        self.len_sudoku = len(data)
        self.is_invalid = False
        if isinstance(self.len_sudoku, float):
            print(self.len_sudoku ** 0.5)
            self.is_invalid = True
        try:
            temporal = int(self.len_sudoku ** 0.5)
            for i in range(self.len_sudoku):
                temporal2 = []
                temporal3 = []
                temporal4 = []
                for j in range(self.len_sudoku):
                    if isinstance(data[i][j], bool) or isinstance(data[i][j], int) != True:
                        self.is_invalid = True
                    elif data[i][j] <= 0 or data[i][j] > self.len_sudoku:
                        self.is_invalid = True
                    temporal2.append(data[i][j])
                    temporal3.append(data[j][i])
                self.columns.append(temporal3)
                self.rows.append(temporal2)
                for ii in range(temporal):
                    for j in range(temporal):
                        temporal4.append(data[(ii + i*temporal) % self.len_sudoku][j + (i*temporal // self.len_sudoku * temporal)])
                self.little_squares.append(temporal4)
        except:
            self.is_invalid = True
    def is_valid(self):
        if self.is_invalid == True:
            print(1)
            return False
        for i in self.columns:
            if len(set(i)) != self.len_sudoku:
                print(2)
                return False
        for i in self.rows:
            if len(set(i)) != self.len_sudoku:
                print(3)
                return False
        for i in self.little_squares:
            if len(set(i)) != self.len_sudoku:
                print(4)
                return False
        else:
            return True


goodSudoku1 = Sudoku([[1,4, 2,3], [3,2, 4,1], [4,1, 3,2], [2,3, 1,4]])

print(goodSudoku1.is_valid())