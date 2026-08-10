import json, time, requests, config


def load_question(path="questions.json"):
    return json.load(open(path, encoding="utf-8"))

def call_api(question, max_retry=3):
    payload = {
        "model": config.MODEL,
        "messages": [{"role":"user", "content":question}],
        "temperature": 0
    }
    for attempt in range(1, max_retry + 1):
        try:
            r = requests.post(config.URL, headers={"Authorization": f"Bearer {config.API_KEY}"}, json=payload, timeout=30)
            return r.json()["choices"][0]["message"]["content"], "ok"
        except Exception as e:
            print(f"失败第{attempt}次：{e}")
            time.sleep(2 * attempt)

    return "", "failed"

def run_batch(questions):
    results = []
    for i, item in enumerate(questions):
        start = time.time()
        answer, status = call_api(item["question"])
        cost = round(time.time() - start, 2)
        results.append({
            "id": item["id"],
            "question": item["question"],
            answer: answer,
            "status": status,
            "cost": cost
        })
        print(f"{i + 1}/{len(questions)} id={item['id']} {status} {cost}s")
        time.sleep(1)

    return results

def save_results(results, path="results.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    questions = load_question()
    answers = run_batch(questions)
    save_results(answers)
    failed = [r for r in answers if answers["status"] == "failed"]
    print(f"完成。成功 {len(answers) - len(failed)} 条，失败 {len(failed)} 条")
