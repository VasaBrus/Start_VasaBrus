seqs = ["ATATACGCGTA", "CTTCGGNGGA"]

print("Последовательность:","".join(seqs))
for seq in seqs:
    for letter in seq:
        print(letter)
    print("-"*20)
print("Цикл завершён")