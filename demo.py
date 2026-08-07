import json, time, requests

url = "https://api.deepseek.com/chat/completions"
headers = {"Authorization": "Bearer sk-cbe6d81da0c64c26ab309c07d0a6939d"}

questions = json.load(open("questions.json",encoding='utf-8'))   # ①从文件读问题
results = []

for i, q in enumerate(questions):               # ②批量循环
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": q}],
        "temperature": 0,
    }
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    answer = r.json()["choices"][0]["message"]["content"]
    results.append({"question": q, "answer": answer})  # ③结果存成列表
    print(f"{i+1}/{len(questions)} 完成")
    time.sleep(1)                                # ④控频

json.dump(results, open("results.json", "w", encoding="utf-8"), ensure_ascii=False)