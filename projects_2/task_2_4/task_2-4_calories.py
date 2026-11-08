protein = float(input("Масса белков в продукте (г): "))
lipid = float(input("Масса жиров в продукте (г): "))
carbohydrate = float(input("Масса углеводов в продукте (г): "))

Cal = (protein * 4) + (lipid * 9) + (carbohydrate * 4)

print(f"Общая калорийность: {Cal}")
