# 项目0：LLM批量评测运行器（地基版）

## 这是什么
从文件读取问题，批量调用大模型API，保存回答并生成运行报告。

## 怎么跑
1. 安装依赖：`pip install requests pytest`
2. 配置密钥：复制 config.py 填入你的 API Key
3. 准备用例：编辑 questions.json（id + question）
4. 运行：`python batch.py` → `python report.py`
5. 看结果：results.json（原始结果）、reports/report.md（报告）

## 对比实验
用 config.MODEL 切换模型，可对比不同模型在同一组问题上的表现（已有 DeepSeek / Qwen 结果）。

## 下一步
- 支持评测指标（准确率、类别统计）
- 支持LLM裁判评分
```

### 第五步：推到 GitHub

仓库已存在，直接推送：

```
git add .
git commit -m "项目0 v1.0：批量调用+容错+pytest+报告+工程整理"
git push
```