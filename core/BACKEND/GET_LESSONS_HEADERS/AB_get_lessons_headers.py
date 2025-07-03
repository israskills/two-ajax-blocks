# === НАСТРОЙКИ ===
URL = "https://www.w3schools.com/js/js_examples.asp"
MAIN_HEADER_FILE = "core/BACKEND/GET_LESSONS_HEADERS/AA_get_main_headers.json"
OUTPUT_FILE = "core/BACKEND/GET_LESSONS_HEADERS/AB_get_lessons_headers.json"
HEADER_TAG = "h2"
BLOCK_TAG = "div"
BLOCK_CLASS = "w3-bar-block"
BUTTON_CLASSES = {"w3-button", "w3-bar-item", "ws-grey"}
# ===================

import requests
from bs4 import BeautifulSoup
import json

# 1. Читаем все заголовки из JSON-файла
with open(MAIN_HEADER_FILE, "r", encoding="utf-8") as f:
    headers = json.load(f)

# 2. Получаем страницу
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

result = {}

# 3. Для каждого заголовка ищем соответствующий блок
for target_header in headers:
    found = False
    for header in soup.find_all(HEADER_TAG):
        if header.get_text(strip=True) == target_header:
            # 4. Ищем соседний div с нужным классом
            next_sibling = header.find_next_sibling()
            while next_sibling and getattr(next_sibling, "name", None) is None:
                next_sibling = next_sibling.next_sibling
            if next_sibling and next_sibling.name == BLOCK_TAG and BLOCK_CLASS in next_sibling.get("class", []):
                # 5. Внутри него ищем кнопки с нужными классами
                buttons = []
                for a in next_sibling.find_all("a"):
                    a_classes = set(a.get("class", []))
                    if BUTTON_CLASSES.issubset(a_classes):
                        buttons.append(a.get_text(strip=True))
                result[target_header] = buttons
                found = True
            break
    if not found:
        result[target_header] = []

# 6. Сохраняем результат в JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    json.dump(result, out, ensure_ascii=False, indent=2)