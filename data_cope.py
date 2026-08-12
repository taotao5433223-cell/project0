import json

data = json.load(open("results.json", encoding="utf-8"))

for item in data:
    item['id'] = int(item['id'])

with open('results.json', 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
