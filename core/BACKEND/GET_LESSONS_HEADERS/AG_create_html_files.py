import os

root_dir = 'core/BACKEND/GET_LESSONS_HEADERS/folder'

for dirpath, dirnames, filenames in os.walk(root_dir):
    index_path = os.path.join(dirpath, 'index.html')
    if not os.path.exists(index_path):
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>index</title>\n</head>\n<body>\n</body>\n</html>')
        print(f'Создан: {index_path}')
    else:
        print(f'Уже существует: {index_path}')