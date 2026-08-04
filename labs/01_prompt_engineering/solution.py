from typing import Iterable, Sequence, Tuple

def build_prompt(task: str, user_input: str, constraints: Iterable[str] = (), examples: Iterable[Tuple[str, str]] = ()) -> str:
    parts = ["你是一名严谨的企业 AI 助手。", f"任务：{task}"]
    examples = list(examples)
    if examples:
        parts.append("示例：" + "；".join(f"输入={x} -> 输出={y}" for x, y in examples))
    constraints = list(constraints)
    if constraints:
        parts.append("约束：" + "；".join(constraints))
    parts.append(f"输入：{user_input}")
    return "\n".join(parts)

def classify_sentiment(text: str) -> str:
    positive = ("好", "满意", "喜欢", "赞")
    negative = ("差", "慢", "退款", "投诉", "失败")
    p, n = sum(w in text for w in positive), sum(w in text for w in negative)
    return "positive" if p > n else "negative" if n > p else "neutral"

def evaluate_predictions(expected: Sequence[str], actual: Sequence[str]) -> float:
    if len(expected) != len(actual) or not expected:
        raise ValueError("两组标签必须非空且等长")
    return sum(a == b for a, b in zip(expected, actual)) / len(expected)
