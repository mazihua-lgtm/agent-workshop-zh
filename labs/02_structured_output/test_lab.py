import json, pytest, solution

def test_valid_ticket():
    t=solution.parse_ticket('{"customer_id":"C1","category":"billing","priority":3,"summary":"扣款"}')
    assert t.priority == 3 and json.loads(solution.to_json(t))["summary"] == "扣款"

@pytest.mark.parametrize("raw", ['{}','{"customer_id":"C1","category":"x","priority":3,"summary":"s"}','{"customer_id":"C1","category":"billing","priority":true,"summary":"s"}'])
def test_invalid_ticket(raw):
    with pytest.raises((ValueError, TypeError)): solution.parse_ticket(raw)
