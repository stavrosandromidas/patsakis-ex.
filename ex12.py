from datetime import date

date1 = str(input("Δώσε ημερομηνία: "))
date1 = date1.replace("/", " ")

today = str(date.today())
today = today.replace("-", " ")
l1 = today.split()
k = l1[0]
p = l1[2]
l1[0] = p
l1[2] = k
today = " ".join(l1)

d = []
today = today.split()
date1 = date1.split()
for i in range(3):
    today[i] = int(today[i])
    date1[i] = int(date1[i])
days = abs(today[0] - date1[0])
months = abs(today[1] - date1[1])
years = abs(today[2] - date1[2])
days_difference = days + (months * 30) + (years * 365)
hours_difference = days_difference * 24
sec_difference = hours_difference * 60
print("Απέχουμε", days_difference, "μέρες,ή", hours_difference, "ώρες,ή", sec_difference, "δευτερόλεπτα.")
if date1 != 2:
    if date1[1] % 2 == 0:
        print("Ο μήνας έχει 30 μέρες.")
    else:
        print("Ο μήνας έχει 31 μέρες.")
else:
    print("Ο μήνας έχει 28 μέρες.")

