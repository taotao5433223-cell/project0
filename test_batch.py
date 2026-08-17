import json, pytest
from batch import parse_answer, save_results

def test_parse_answer_Normal():
    resp = {
        "choices":[{
            "message":{
                "content":"你好"
            }
        }]
    }
    assert parse_answer(resp) == "你好"

def test_parse_answer_NoChoices():
    with pytest.raises(KeyError):
        parse_answer({"error": {"message": "invalid api key"}})

def test_parse_answer_ChoiceFirst():
    resp = {
        "choices": [
            {"message":{"content":"First Message."}},
            {"message":{"content":"Second Message."}}
        ]}
    assert parse_answer(resp) == "First Message."

def test_save_resultd_file(tmp_path):
    results = [{
        "id": 1,
        "question": "测试",
        "answer": "回答",
        "status": "ok",
        "cost_time": 1.0
    }]
    out = tmp_path / "r.json"
    save_results(results,out)
    data = json.load(open(out, encoding="utf-8"))
    assert data[0]["id"] == 1
    assert data[0]["answer"] == "回答"
