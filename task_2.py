# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ = not ⋁ = or ⋀ = and
# ¬(X ⋁ Y ⋁ Z) == not(X or Y or Z)

x=int(input("Введите число х: "))
y=int(input("Введите число y: "))
z=int(input("Введите число z: "))
if (not(x or y or z)) == (not x and not y and not z):
    print(True)
else:
    print(False)