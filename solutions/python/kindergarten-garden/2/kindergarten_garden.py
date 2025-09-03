grade12 = ["Alice", "Bob", "Charlie","David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
class Garden:
    def __init__(self, diagram, students=grade12):
      self.diagram = diagram
      self.students = sorted(students)

    def plants(self, student):
      student_index = self.students.index(student) * 2
      row_plant_1 = []
      row_plant_2 = []
      new_diagram = self.diagram.split("\n")
      row_1 = new_diagram[0]
      row_2 = new_diagram[1]
      for _ in range(2):
        row_plant_1.append(row_1[student_index])
        row_plant_2.append(row_2[student_index])
        student_index += 1
      student_plant = row_plant_1 + row_plant_2
      return convert(student_plant)

def convert(plants):
  student_plant = []
  plant_dict = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
  for letter in plants:
    student_plant.append(plant_dict[letter])
  return student_plant
