import json

ab_path = "core/BACKEND/GET_LESSONS_HEADERS/AB_get_lessons_headers.json"
ac_path = "core/BACKEND/GET_LESSONS_HEADERS/AC_create_folder_names.json"
ad_path = "core/FRONTEND/JAVASCRIPT/javascript_headers.json"

with open(ab_path, encoding="utf-8") as f:
    ab = json.load(f)
with open(ac_path, encoding="utf-8") as f:
    ac = json.load(f)

ab_keys = list(ab.keys())
ac_keys = list(ac.keys())

result = []
for ab_key, ac_key in zip(ab_keys, ac_keys):
    ab_list = ab[ab_key]
    ac_list = ac[ac_key]
    children = []
    for h, f in zip(ab_list, ac_list):
        children.append({"header": h, "folder": f})
    result.append({
        "header": ab_key,
        "folder": ac_key,
        "children": children
    })

with open(ad_path, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Combined headers written to {ad_path}")