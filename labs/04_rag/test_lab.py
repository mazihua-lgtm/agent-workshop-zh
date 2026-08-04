import solution

def test_chunk_and_retrieve_with_citation():
    idx=solution.build_index({"a.md":"生产访问必须启用 MFA。","b.md":"食堂周五供应面条。"},20,2)
    hits=solution.retrieve("生产访问 MFA",idx,1)
    assert hits and hits[0][1].source == "a.md"
    assert "[a.md]" in solution.answer("问题",hits)

def test_no_evidence_and_overlap_validation():
    assert "无法回答" in solution.answer("x",[])
    try: solution.chunk_text("abc",3,3)
    except ValueError: pass
    else: raise AssertionError("应拒绝 overlap >= chunk_size")
