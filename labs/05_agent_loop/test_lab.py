import pytest, solution

def test_agent_loop_and_eval():
    result=solution.run_agent("计算 2+3，然后查询上海天气",4)
    assert len(result["trace"]) == 2
    score=solution.evaluate_trace(result["trace"],{"calculator","weather"})
    assert score["tool_coverage"] == 1 and score["errors"] == 0

def test_guardrails():
    with pytest.raises(ValueError): solution.execute("delete_all","x")
    result=solution.run_agent("计算 1+1，查询上海天气",1)
    assert result["stopped"] and len(result["trace"]) == 1
