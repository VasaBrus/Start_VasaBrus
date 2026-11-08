reagent_name = input("Введите название реактива: ")
reagent_amount = int(input("Введите количество (целое число): "))
inventory_control = open("inventory.txt", "w", encoding="utf-8")

print(f"Реактив {reagent_name} поступил на склад в количестве {reagent_amount} шт.", file=inventory_control) # Сохраняем отчёт в файл
inventory_control.close()

print("="*40)
print(f"Реактив {reagent_name} поступил на склад в количестве {reagent_amount} шт.") # Выводим отчёт в термиал
print("="*40)