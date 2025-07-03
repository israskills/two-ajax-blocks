import subprocess

scripts = [
    "core/BACKEND/GET_LESSONS_HEADERS/AA_get_main_headers.py",
    "core/BACKEND/GET_LESSONS_HEADERS/AB_get_lessons_headers.py",
    "core/BACKEND/GET_LESSONS_HEADERS/AC_create_folder_names.py",
    "core/BACKEND/GET_LESSONS_HEADERS/AD_check_repeated_names.py",
    "core/BACKEND/GET_LESSONS_HEADERS/AE_create_folders.py"
]

for script in scripts:
    print(f"Запуск {script} ...")
    subprocess.run(["python", script])