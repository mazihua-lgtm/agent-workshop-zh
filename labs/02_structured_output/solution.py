import json
from dataclasses import asdict, dataclass

TICKET_SCHEMA = {"type":"object","required":["customer_id","category","priority","summary"],"properties":{"customer_id":{"type":"string"},"category":{"enum":["billing","technical","other"]},"priority":{"type":"integer","minimum":1,"maximum":5},"summary":{"type":"string"}},"additionalProperties":False}

@dataclass(frozen=True)
class Ticket:
    customer_id: str
    category: str
    priority: int
    summary: str

def parse_ticket(raw: str) -> Ticket:
    data=json.loads(raw)
    allowed=set(TICKET_SCHEMA["properties"])
    if set(data) != allowed:
        raise ValueError("字段必须与 schema 完全一致")
    if data["category"] not in {"billing","technical","other"}: raise ValueError("非法 category")
    if type(data["priority"]) is not int or not 1 <= data["priority"] <= 5: raise ValueError("priority 必须为 1-5 整数")
    if not all(isinstance(data[k],str) and data[k].strip() for k in ("customer_id","summary")): raise ValueError("文本字段不能为空")
    return Ticket(**data)

def to_json(ticket: Ticket) -> str:
    return json.dumps(asdict(ticket), ensure_ascii=False, sort_keys=True)
