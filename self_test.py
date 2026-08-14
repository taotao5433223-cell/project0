"""
1、加载数据
2、获取测试API
3、批处理
4、保存结果
"""

import json, time, requests, config

# 加载数据
def load_questions(path="questions_test.json"):
    return json.load(open(path, encoding="utf-8"))

#获取测试API
def call_api(question, max_try=3):
    payload = {
        "model": config.MODEL,
        "messages": [{"role":"user","content":question}],
        "temperature": 0
    }
    for i in range(1, max_try + 1):
        try:
            r = requests.post(config.URL, headers={"Authorization": f"Bearer {config.API_KEY}"}, json=payload, timeout=100)
            return r.json()["choices"][0]["message"]["content"], "ok"
        except Exception as e:
            print(f"第{i}次失败:{e}")
            time.sleep(2 * i)

    return "", "failed"

#批量处理
def run_batch():
    results = []
    questions = load_questions()
    for i,item in enumerate(questions):
        start = time.time()
        answer,status = call_api(item["question"])
        cost = round(time.time() - start, 2)
        results.append({
            "id": item["id"],
            "question": item["question"],
            "answer": answer,
            "status": status,
            "cost": cost
        })
        print(f"已完成{i + 1}/{len(questions)}, id={item['id']}, status={status}, cost={cost}s")
        time.sleep(1)

    return results

# 保存结果
def save_results(results):
    with open("self_test_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    results = run_batch()
    save_results(results)
    failed = [r for r in results if r["status"] == "failed"]
    print(f"成功{len(results)-len(failed)}条,失败{len(failed)}条")