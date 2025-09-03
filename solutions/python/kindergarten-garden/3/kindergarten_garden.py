grade12 = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Fred",
    "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
]

class Garden:
    plant_dict = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    def __init__(self, diagram, students=grade12):
        self.rows = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, student):
        i = self.students.index(student) * 2
        letters = [row[i:i+2] for row in self.rows]  # grab 2 cups from each row
        return [self.plant_dict[ch] for row in letters for ch in row]

