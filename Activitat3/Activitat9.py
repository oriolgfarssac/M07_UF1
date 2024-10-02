#Versio 1
assignatures = ['Matemàtiques', 'Llengua', 'Ciències', 'Història', 'Anglès', 'Educació Física']

notes = []

for i in range(len(assignatures)):
    nota = float(input(f"Quina nota has tret a {assignatures[i]}? "))
    notes.append(nota)

print(assignatures)
print(notes)


#Versio 2
notes_assig = {
    'Matemàtiques': None,
    'Llengua': None,
    'Ciències': None,
    'Història': None,
    'Anglès': None,
    'Educació Física': None
}

for assignatura in notes_assig:
        notes_assig[assignatura] = float(input(f"Quina nota has tret a {assignatura}? "))

print(notes_assig)
