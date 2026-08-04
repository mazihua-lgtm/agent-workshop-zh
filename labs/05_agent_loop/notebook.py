# %% [markdown]
# # Lab 05 · Agent Loop
# 实现一个可观察、可限制、可评测的 Agent Loop：规划动作、执行白名单工具、记录 observation，并通过最大步数与敏感操作 guardrail 防止失控。对比 ReAct 与 Plan-and-Execute 的控制点。
# %%
from solution import run_agent, evaluate_trace

result=run_agent("计算 2+3，然后查询上海天气", max_steps=4)
print(result["answer"])
for event in result["trace"]: print(event)
print(evaluate_trace(result["trace"], required_tools={"calculator","weather"}))
