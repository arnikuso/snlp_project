file1 = 'labour.txt' 
file2 = 'tories.txt'
output_file = "corpus.txt"
validation_file = "validation.txt"



with open(file1, "r", encoding="utf-8") as f1:
    lines1 = [line.strip() for line in f1 if line.strip()]

with open(file2, "r", encoding="utf-8") as f2:
    lines2 = [line.strip() for line in f2 if line.strip()]

min_len = min(len(lines1), len(lines2))
val_count = max(1, int(min_len * 0.05))

trimmed1 = lines1[:min_len]
trimmed2 = lines2[:min_len]

train1 = trimmed1[:-val_count]
val1 = trimmed1[-val_count:]

train2 = trimmed2[:-val_count]
val2 = trimmed2[-val_count:]


with open(output_file, "w", encoding="utf-8") as out:
    for line in train1:
        out.write(f"<01> {line}\n")
    out.write("\n")
    for line in train2:
        out.write(f"<02> {line}\n")


with open(validation_file, "w", encoding="utf-8") as val_out:
    for line in val1:
        val_out.write(f"<01> {line}\n")
    val_out.write("\n")
    for line in val2:
        val_out.write(f"<02> {line}\n")

print(f"Готово. Тренировочный корпус: {output_file}")
print(f"Validation корпус: {validation_file}")