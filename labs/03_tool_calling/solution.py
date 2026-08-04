import ast, operator
from typing import Any, Dict

_WEATHER={"上海":{"condition":"多云","temperature_c":26},"北京":{"condition":"晴","temperature_c":29}}
_CUSTOMERS={"C001":{"tier":"enterprise","status":"active"},"C002":{"tier":"standard","status":"paused"}}
_OPS={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.USub:operator.neg}

def _eval(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int,float): return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS: return _OPS[type(node.op)](_eval(node.left),_eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS: return _OPS[type(node.op)](_eval(node.operand))
    raise ValueError("仅支持基础算术")

def calculator(expression: str): return _eval(ast.parse(expression, mode="eval").body)
def weather(city: str):
    if city not in _WEATHER: raise KeyError("无该城市离线天气")
    return {"city":city, **_WEATHER[city]}
def database_query(customer_id: str):
    if customer_id not in _CUSTOMERS: raise KeyError("客户不存在")
    return {"customer_id":customer_id, **_CUSTOMERS[customer_id]}
def dispatch(name: str, arguments: Dict[str, Any]):
    tools={"calculator":calculator,"weather":weather,"database_query":database_query}
    if name not in tools: return {"ok":False,"error":"unknown_tool"}
    try: return {"ok":True,"result":tools[name](**arguments)}
    except (KeyError,TypeError,ValueError,ZeroDivisionError) as exc: return {"ok":False,"error":str(exc)}
def tool_specs():
    return [{"name":"calculator","description":"安全计算基础算术"},{"name":"weather","description":"查询离线示例天气"},{"name":"database_query","description":"按客户 ID 只读查询"}]
