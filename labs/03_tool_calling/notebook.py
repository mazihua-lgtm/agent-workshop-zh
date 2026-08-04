# %% [markdown]
# # Lab 03 · Tool Calling
# Function calling 不是让模型直接执行代码，而是让模型产生受约束的调用意图，再由应用完成白名单校验、执行和错误封装。本 Lab 注册计算器、天气和只读数据库三个工具。
# %%
from solution import dispatch, tool_specs

print([x["name"] for x in tool_specs()])
print(dispatch("calculator", {"expression":"(12 + 8) * 3"}))
print(dispatch("weather", {"city":"上海"}))
print(dispatch("database_query", {"customer_id":"C001"}))
