n = int(input())
mass = 0
charge = 0
for i in range(n):
    mass += int(input())
    charge += int(input())
m = int(input())
for i in range(m):
    mass -= int(input())
    charge -= int(input())
print("Масса ядра: " + str(mass) + " а.е.м.", "Заряд ядра: " + str(charge) + " e", sep="\n")
