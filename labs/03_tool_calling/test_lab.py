import solution

def test_three_tools():
    assert len(solution.tool_specs()) == 3
    assert solution.dispatch("calculator",{"expression":"2+3*4"})["result"] == 14
    assert solution.dispatch("weather",{"city":"上海"})["result"]["temperature_c"] == 26
    assert solution.dispatch("database_query",{"customer_id":"C001"})["result"]["status"] == "active"

def test_guardrails():
    assert not solution.dispatch("calculator",{"expression":"__import__('os')"})["ok"]
    assert solution.dispatch("delete_database",{})["error"] == "unknown_tool"
