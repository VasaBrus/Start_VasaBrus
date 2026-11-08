amount = float(input("Введите общее количество произведенных капсул: "))
amount_capsules = float(input("Введите количество капсул в одной упаковке: "))

full_package = amount // amount_capsules
remainder = amount % amount_capsules
print("-"*3, "Отчет фасовочного цеха", "-"*3, sep=" ")
print(f"Полных упаковок: {full_package:.0f} шт.")
print(f"Остаток капсул: {remainder:.0f} шт.")