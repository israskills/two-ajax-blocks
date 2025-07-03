import os
import json

ROOT = "core/BACKEND/GET_LESSONS_HEADERS/folder"  # Название корневой папки
JSON_PATH = "core/BACKEND/GET_LESSONS_HEADERS/AC_create_folder_names.json"  # Путь к вашему JSON-файлу

def main():
    # Чтение JSON
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Создание корневой папки
    os.makedirs(ROOT, exist_ok=True)

    for category, items in data.items():
        category_path = os.path.join(ROOT, category)
        os.makedirs(category_path, exist_ok=True)
        for item in items:
            item_path = os.path.join(category_path, item)
            os.makedirs(item_path, exist_ok=True)

if __name__ == "__main__":
    main()