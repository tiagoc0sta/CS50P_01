# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Gryffindor",
# }

# for student in students:
#     print(student)

students = []

with open("studens.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

        def get_name(student):
            return student["name"]

        for student in sorted(students):
            print(f"{student['name']} is in {student['house']}")
