class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(num) for num in row.split()]
            for row in matrix_string.split("\n")
            ]

    def row(self, index):
      if index > len(self.rows):
        raise ValueError(f"The row does not exist.\n Please enter a number between 1 and {len(self.rows)}")
      return self.rows[index-1]


    def column(self, index):
      column_counter = len(self.rows[0])
      if index > column_counter:
        raise ValueError(f"The column does not exist.\n Please enter a number between 1 and {column_counter}")
      return [column[index-1] for column in self.rows]

