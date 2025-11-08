# Es 1
"""
1. Chiediamo il numero di studenti da inserire
2. Chiediamo all'utente di inserire il nome degli studenti e i loro voti
3. Memorizziamo queste informazioni utilizzando una lista di dizionari dove ogni dizionario contiene il nome e il voto dello studente
4. Stampiamo i dettagli degli studenti e i loro voti
"""

students = []
student_number = int(input("Quanti studenti vuoi inserire?\n"))

for _ in range(student_number):

  student = {}

  student_name = input("Digita il nome completo dello studente:\n").strip()
  student_score = int(input("Inserire il voto dello studente:\n"))

  student["name"] = student_name
  student["score"] = student_score

  students.append(student)

  print(f"Studente {student['name']} con voto {student['score']} aggiunto.\n")

print("\nStampa di tutti gli studenti\n")

for position, student in enumerate(students):
  print(f"{position + 1}. {student['name']} - {student['score']}")