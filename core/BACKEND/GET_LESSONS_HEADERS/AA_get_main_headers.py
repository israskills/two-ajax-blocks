# === НАСТРОЙКИ ===
URL = "https://www.w3schools.com/js/js_examples.asp"  # Ссылка для парсинга
OUTPUT_FILE = "core/BACKEND/GET_LESSONS_HEADERS/AA_get_main_headers.json"  # Имя файла для вывода
HEADER_TAG = "h2"                                      # Какой тег искать как заголовок
BLOCK_TAG = "div"                                      # Какой тег считать блоком после заголовка
BLOCK_CLASS = "w3-bar-block"                           # Класс блока после заголовка
# ===================

import requests
from bs4 import BeautifulSoup
import json

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

result = []
for header in soup.find_all(HEADER_TAG):
    next_sibling = header.find_next_sibling()
    # Пропускаем пустые строки между тегами
    while next_sibling and getattr(next_sibling, "name", None) is None:
        next_sibling = next_sibling.next_sibling
    if next_sibling and next_sibling.name == BLOCK_TAG and BLOCK_CLASS in next_sibling.get("class", []):
        result.append(header.get_text(strip=True))

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)