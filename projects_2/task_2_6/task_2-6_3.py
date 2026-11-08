donor = input("Введите группу крови донора (например, A, B, AB, O): ").strip().upper()
patient = input("Введите группу крови пациента (например, A, B, AB, O): ").strip().upper()

valid_groups = ("A", "B", "AB", "O")

if donor not in valid_groups or patient not in valid_groups:
    print("Ошибка: допустимые группы крови — A, B, AB, O.")
elif donor == patient or donor == "O":
    print(f"Переливание возможно.")
elif donor == "A" and patient == "AB":
    print("Переливание возможно.")
elif donor == "B" and patient == "AB":
    print("Переливание возможно.")
else:
    print(f"Переливание НЕВОЗМОЖНО!")