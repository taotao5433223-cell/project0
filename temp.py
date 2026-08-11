#加载问题——>调用API——>分批次处理——>保存结果
import json, requests, time, config

def questions(path="questions.json"):
    return json.load(open(path, encoding="utf-8"))

def call_api(question, max_try=3):
    payload = {
        "model": config.MODEL,
        "messages": [{"role":"user","content":question}],
        "temperature": 0
    }

    for attempt in range(1, max_try + 1):
        try:
            r = requests.post(config.URL, json=payload, timeout=30)
            return r.json()["choices"][0]["message"]["content"], "ok"
        except Exception as e:
            print(f'失败第{attempt}次：{e}')

    return "", "Failed"


def run_batch(questions):
    results_temp = []
    for i, item in enumerate(questions):
        start = time.time()
        answer, status = call_api(item["question"])
        cost = round(time.time() - start, 2)
        results_temp.append({
            "id":item["id"],
            "question":item["question"],
            "answer":answer,
            "status":status,
            "cost":cost
        })
        print(f"{i + 1}/{len(questions)} id={item['id']} {status} {cost}s")
        time.sleep(1)

    return results_temp


def save_results(results):
    with open("results_temp.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    questions = questions()
    results = run_batch(questions())
    save_results(results)
    failed = [r for r in results if r["status"] == "failed"]
    print(f"完成。成功 {len(results) - len(failed)} 条，失败 {len(failed)} 条")