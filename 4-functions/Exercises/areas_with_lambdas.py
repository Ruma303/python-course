"""
- Sviluppare un'applicazione per calcolare l'area di una forma geometrica.
- L'utente avrà la possibilità di scegliere tra quadrato, un rettangolo, un cerchio, inserendo le dimensioni appropriate.
- L'applicazione calcolerà quindi l'area corrispondente e la restituirà all'utente.
- Utilizzare le funzioni lambda per calcolare le aree.
"""

import math

shape = input("Scegli una forma geometrica digitando quadrato, rettangolo o cerchio (oppure 'q' per uscire):\n").strip().lower()

while shape != "q":
    match shape:
        case "quadrato":
            lato = int(input("Inserisci il valore del lato:\n"))
            area_quadrato = lambda lato: lato ** 2
            print("L'area del quadrato è:", area_quadrato(lato))
        case "rettangolo":
            lato_minore = int(input("Inserisci il valore del lato minore:\n"))
            lato_maggiore = int(input("Inserisci il valore del lato maggiore:\n"))
            area_rettangolo = lambda x, y: x * y
            print("L'area del rettangolo è:", area_rettangolo(lato_minore, lato_maggiore))
        case "cerchio":
            raggio = int(input("Inserisci il valore del raggio:\n"))
            area_cerchio = lambda r: math.pi * r ** 2
            print("L'area del cerchio è:", area_cerchio(raggio))
        case _:
            print("Non hai fatto una scelta o non è corretta. Riprova o digita 'q' per uscire.")
    shape = input("Scegli una forma geometrica digitando quadrato, rettangolo o cerchio (oppure 'q' per uscire):\n").strip().lower()

print("Grazie per aver usato l'applicazione. A presto!")