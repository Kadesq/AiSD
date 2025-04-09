def are_ascii(c1, c2):
    if len(c1) > 0 and len(c2) > 0:
        return abs(ord(c1) - ord(c2)) == 1 and ord(c1) < 128 and ord(c2) < 128
    return False


f = open('zadanie2.csv', 'r', encoding='utf-8')

txt = f.read()
print(txt)
print('---')

lines = txt.splitlines()
print(lines)
print('###')

f.close()

header = lines[0]

lines_data = []

for line in lines[1:]:
    columns = line.split(',')
    if len(columns) > 1 and columns[1].strip():
        lines_data.append(columns)

for i in range(len(lines_data)):
    for j in range(i + 1, len(lines_data)):
        try:
            if int(lines_data[i][0]) > int(lines_data[j][0]):
                lines_data[i], lines_data[j] = lines_data[j], lines_data[i]
        except ValueError:
            continue

last_id = 0
for i in range(len(lines_data)):
    try:
        current_id = int(lines_data[i][0])
    except ValueError:
        current_id = last_id + 1
    if current_id <= last_id:
        current_id = last_id + 1
        lines_data[i][0] = str(current_id)
    last_id = current_id

for i in range(len(lines_data)):
    for j in range(len(lines_data[i])):
        lines_data[i][j] = lines_data[i][j].lower()

removed_words = []

def remove_words(columns):
    new_columns = []
    for word in columns:
        if len(word) > 1 and are_ascii(word[0], word[1]):
            removed_words.append(word)
        else:
            new_columns.append(word)
    return new_columns

for i in range(len(lines_data)):
    lines_data[i] = remove_words(lines_data[i])

f = open('zadanie2_filtered.csv', 'w', encoding='utf-8')
f.write(header + "\n")

for line in lines_data:
    f.write(",".join(line) + "\n")

f.close()

for word in removed_words:
    print(f"Usunięty wyraz: {word}")
