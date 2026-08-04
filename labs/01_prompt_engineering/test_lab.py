import solution

def test_prompt_contains_contract():
    p=solution.build_prompt("分类", "样本", ["仅 JSON"], [("a","b")])
    assert all(x in p for x in ("任务：分类","输入：样本","仅 JSON","a -> 输出=b"))

def test_sentiment_and_eval():
    assert solution.classify_sentiment("我很满意") == "positive"
    assert solution.classify_sentiment("退款太慢") == "negative"
    assert solution.evaluate_predictions(["a","b"],["a","x"]) == .5
