# === НАСТРОЙКИ ===
INPUT_FILE = 'core/BACKEND/GET_LESSONS_HEADERS/AB_get_lessons_headers.json'      # Входной файл
OUTPUT_FILE = 'core/BACKEND/GET_LESSONS_HEADERS/AC_create_folder_names.json'     # Выходной файл
TRANSFORM_KEYS = True                           # Преобразовывать ключи
TRANSFORM_VALUES = True                         # Преобразовывать строки внутри массивов
# ===================

import json
import re

# Словарь для замены символов на слова
REPLACE_SIGNS = {
    '+': 'plus',
    '-': 'minus',
    '*': 'times',
    '/': 'divided-by',
    '%': 'mod',
    '=': 'equals',
    '<': 'less-than',
    '>': 'greater-than',
    '&': 'and',
    '|': 'or',
    '!': 'not',
    '^': 'xor',
    '~': 'tilde',
    '?': 'question',
    ':': 'colon',
    '.': 'dot',
    ',': 'comma',
    '(': '',
    ')': '',
    '[': '',
    ']': '',
    '{': '',
    '}': '',
    '"': '',
    "'": '',
    '`': '',
}

def replace_signs_with_words(text):
    # Сначала заменяем все знаки на слова, окружая пробелами для разделения
    for sign, word in REPLACE_SIGNS.items():
        text = text.replace(sign, f' {word} ')
    return text

def slugify(text):
    text = replace_signs_with_words(text)
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

with open(INPUT_FILE, 'r', encoding='utf-8') as infile:
    data = json.load(infile)

result = {}
for k, v in data.items():
    new_key = slugify(k) if TRANSFORM_KEYS else k
    if isinstance(v, list) and TRANSFORM_VALUES:
        new_list = [slugify(item) if isinstance(item, str) else item for item in v]
        result[new_key] = new_list
    else:
        result[new_key] = v

with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
    json.dump(result, outfile, ensure_ascii=False, indent=2)

print(f"Готово! Сохранено в {OUTPUT_FILE}")