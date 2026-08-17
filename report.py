import json, os

def load_results(path="results.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def build_report(results):
    total = len(results)
    ok = [r for r in results if r["status"] == "ok"]
    failed = [r for r in results if r["status"] != "ok"]
    success_rate = round(len(ok) / total * 100, 2) if total else 0

    avg_time = round(sum(r["cost_time"] for r in ok) / len(ok), 2) if ok else 0

    lines = []
    lines.append("# 评测运行报告")
    lines.append(f"- 总用例数：{total}")
    lines.append(f"- 成功数：{len(ok)}")
    lines.append(f"- 失败数：{len(failed)}")
    lines.append(f"- 成功率：{success_rate}%")
    lines.append(f"- 平均耗时：{avg_time}s")
    lines.append("")
    lines.append("## 失败样例")
    for r in failed[:5]:
        lines.append(f"- id={r['id']}：{r['question'][:30]} ... 状态={r['status']}")
    return "\n".join(lines)


if __name__ == "__main__":
    results = load_results()
    report = build_report(results)
    print(report)
    os.makedirs("reports", exist_ok=True)
    with open(os.path.join("reports", "report.md"), "w", encoding="utf-8") as f:
        f.write(report)
    print("\n报告已保存到 reports/report.md")