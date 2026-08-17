import json

data = json.load(open("results.json", encoding="utf-8"))
temp = []

for item in data:
    d = {k.replace("cost", "cost_time"):v for k,v in item.items()}
    temp.append(d)

json.dump(temp, open("results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
