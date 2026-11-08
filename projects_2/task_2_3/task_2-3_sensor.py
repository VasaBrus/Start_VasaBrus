operator_name = input("Введите имя оператора: ")
pressure_sensor = input("Введите текущее значение давления: ")

with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"Введите имя оператора: {operator_name}\n")
    file.write(f"Введите текущее значение давления: {pressure_sensor}\n")
    file.write("Данные успешно сохранены в sensor_log.txt")

print("Данные успешно сохранены в sensor_log.txt")