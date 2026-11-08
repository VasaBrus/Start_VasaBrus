print("="*3, "Анализ последовательности ДНК", "="*3, sep=" ")
dna = input("Введите последовательность ДНК: ").upper()
print(f"Последовательность в верхнем регистре: {dna}")

count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")
count_dna = count_A + count_T + count_G + count_C
perc_A = (count_A / count_dna)*100
perc_T = (count_T / count_dna)*100
perc_G = (count_G / count_dna)*100
perc_C = (count_C / count_dna)*100

print("="*40)
print("Подсчёт нуклеотидов:")
print(f"A: {count_A} ({perc_A:.1f}% последовательности)")
print(f"T: {count_T} ({perc_T:.1f}% последовательности)")
print(f"G: {count_G} ({perc_G:.1f}% последовательности)")
print(f"C: {count_C} ({perc_C:.1f}% последовательности)")
print(f"Общая длина: {count_dna}")
print("="*40)