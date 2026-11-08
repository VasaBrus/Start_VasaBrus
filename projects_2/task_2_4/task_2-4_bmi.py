weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))

bmi = weight / (height ** 2)

print("-"*3, "Отчет о состоянии здоровья", "-"*3, sep=" ")
print(f"Рост:\t{height} м")
print(f"Вес:\t{weight} кг")
print(f"Индекс массы тела пациента: {bmi:.2f}")