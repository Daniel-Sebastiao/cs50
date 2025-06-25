students = {
    "Harry": "Gryffindor",
    "Ron": "Slytherin",
    "Hermione": "Gryffindor",
    "Draco": "Gryffindor",
}

#for student in students:
   # print(f"{student} - {students[student]}")


hog_students = [
    {'name': "Hermione", 'house': "Gryffindor", 'patronus': 'Otter'},
    {'name': "Harry",'house': "Gryffindor",'patronus': 'Stag'},
    {'name': "Ron", 'house': "Gryffindor", 'patronus': 'Jack Russell terrier'},
    {'name': "Draco", 'house': "Gryffindor", 'patronus': None}
]

for student in hog_students:
    print(student['name'], student['house'], student['patronus'], sep=" - ")



