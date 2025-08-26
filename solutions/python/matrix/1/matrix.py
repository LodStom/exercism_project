class Matrix:
    def __init__(self, matrix_string):
        # Parse the string once into a list of lists of ints
        self.rows = [
            [int(num) for num in row.split()]
            for row in matrix_string.split("\n")
        ]

    def row(self, index):
        # Just return the (index-1)th row
        return self.rows[index - 1]

    def column(self, index):
        # Collect the (index-1)th element from each row
        return [row[index - 1] for row in self.rows]


