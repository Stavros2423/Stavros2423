x = int(input("Δώσε Βάρος:"))
y = int(input("Δώσε ύψος:"))

bmi = (x / (y ** 0.5))

if bmi < 19:
    print("Λιποβαρής")

elif 19 <= bmi <= 25:
    print("Κανονικό Βάρος")

elif 26 <= bmi <=29:
    print("Υπέρβαρος")

elif 30 <= bmi <= 34:
    print("Παχύσαρκος")

else:
    print("Σοβαρά Παχύσαρκου")
