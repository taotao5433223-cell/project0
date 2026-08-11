import json, time, requests, config

url = config.URL
headers = {"Authorization": f"Bearer {config.API_KEY}"}
results_temp = []

questions = json.load(open("questions_temp.json", encoding="utf-8"))

for i, item in enumerate(questions):
    payload = {
        "model": config.MODEL,
        "messages": [{"role":"user","content":item["question"]}],
        "temperature": 0
    }
    r = requests.post(url, json=payload, headers=headers)
    answer = r.json()["choices"][0]["message"]["content"]
    results_temp.append({
        "id": item["id"],
        "question": item["question"],
        "answer": answer
    })

    print(f"{1+i}/{len(questions)}已完成")
    time.sleep(1)

with open("results_temp.json", "w", encoding="utf-8") as f:
    json.dump(results_temp, f, ensure_ascii=False, indent=2)