# Example of dictionary
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slyntherin",
# }

# for student in students:
#     print(student, students[student], sep=", ")


# example of list of dictionary
students = [
    {"name": "Hermione", "house": "Gryffindor", "patrous": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patrous": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patrous": "Jack"},
    {"name": "Draco", "house": "Slyntherin", "patrous": None},
]

for s in students:
    print(s["name"], s["house"], s["patrous"], sep=", ")
