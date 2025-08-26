class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
      self.matrix_string = self.matrix_string.split("\n")
      rows = []
      int_row = []
      for row in self.matrix_string:
        rows.append(row.split())
      return [int(num) for num in rows[index-1]]


    def column(self, index):
      thee_rows = row_for_column(self.matrix_string)
      return [int(colum[index-1]) for colum in thee_rows]

def row_for_column(mtrx_str):
      mtrx_str = mtrx_str.split("\n")
      rows = []
      for row in mtrx_str:
        rows.append(row.split())
      return rows

