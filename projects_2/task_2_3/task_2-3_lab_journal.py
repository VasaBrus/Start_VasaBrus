fio = input("ФИО: ")
date = input("Дата: ")
exp = input("Эксперимент: ")
result = input("Вывод: ")

width = 60
border = "+" + "-"*width + "+"

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(border + "\n")
    file.write("| " + "Электронный лабораторный журнал".ljust(width - 2) + " |\n")
    file.write(border + "\n")
    file.write("| " + f"ФИО исследователя : {fio}".ljust(width - 2) + " |\n")
    file.write("| " + f"Дата : {date}".ljust(width - 2) + " |\n")
    file.write("| " + f"Эксперимент : {exp}".ljust(width - 2) + " |\n")
    file.write(border + "\n")
    file.write("| " + "Вывод:".ljust(width - 2) + " |\n")
    file.write("| " + result.ljust(width - 2) + " |\n")
    file.write(border + "\n")