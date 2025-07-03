import re

filename = "core/BACKEND/GET_LESSONS_HEADERS/AC_create_folder_names.json"
with open(filename, encoding="utf-8") as f:
    lines = f.readlines()

seen = {}
new_lines = []

for line in lines:
    # Строго ищем строки, где только значение в массиве (без ключа)
    match = re.match(r'(\s*)"([^"]+)"(,?)\s*$', line)
    if match:
        indent, text, comma = match.groups()
        count = seen.get(text, 0)
        if count == 0:
            new_lines.append(line)
        else:
            new_text = f'"{text}{count+1}"{comma}\n'
            new_lines.append(f"{indent}{new_text}")
        seen[text] = count + 1
    else:
        # Все остальные строки (ключи, скобки и т.д.) оставляем как есть
        new_lines.append(line)

with open(filename, "w", encoding="utf-8") as f:
    f.writelines(new_lines)