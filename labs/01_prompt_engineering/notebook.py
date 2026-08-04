# %% [markdown]
# # Lab 01 · Prompt Engineering
# 把 prompt 当作可测试的软件接口：明确角色、任务、约束、示例与输出格式，并比较 zero-shot、few-shot 与显式推理步骤。Claude / GPT 的差异应通过同一评测集实测，而不是凭印象下结论。
# %%
from solution import build_prompt, classify_sentiment, evaluate_predictions

prompt = build_prompt("将客户反馈分类", "退款太慢了", constraints=["只输出 positive/neutral/negative"], examples=[("很好用", "positive")])
print(prompt)
print(classify_sentiment("退款太慢了"))
print(evaluate_predictions(["positive", "negative"], ["positive", "neutral"]))
