# %% [markdown]
# # Lab 02 · Structured Output
# 用 JSON Schema 定义接口契约，用 Pydantic 做生产校验；离线版本提供标准库校验器，安装 Pydantic 后可替换为 BaseModel。重点是拒绝不完整、类型错误和多余字段。
# %%
from solution import TICKET_SCHEMA, parse_ticket, to_json

raw = '{"customer_id":"C-1024","category":"billing","priority":2,"summary":"重复扣款"}'
ticket = parse_ticket(raw)
print(ticket)
print(to_json(ticket))
print(TICKET_SCHEMA)
