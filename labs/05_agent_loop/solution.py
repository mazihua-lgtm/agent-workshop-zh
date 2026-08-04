import ast, operator

OPS={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv}
def safe_calc(expr):
    def ev(n):
        if isinstance(n,ast.Constant) and type(n.value) in (int,float): return n.value
        if isinstance(n,ast.BinOp) and type(n.op) in OPS: return OPS[type(n.op)](ev(n.left),ev(n.right))
        raise ValueError("unsafe expression")
    return ev(ast.parse(expr,mode="eval").body)
def plan(task):
    actions=[]
    if "计算" in task: actions.append(("calculator",task.split("计算",1)[1].split("，",1)[0].strip()))
    for city in ("上海","北京"):
        if city in task and "天气" in task: actions.append(("weather",city))
    return actions
def execute(tool,arg):
    if tool=="calculator": return safe_calc(arg)
    if tool=="weather": return {"上海":"多云 26°C","北京":"晴 29°C"}[arg]
    raise ValueError("tool not allowed")
def run_agent(task,max_steps=5):
    if max_steps < 1: raise ValueError("max_steps must be positive")
    trace=[]
    for tool,arg in plan(task)[:max_steps]:
        trace.append({"thought":"选择满足子任务的最小工具","action":tool,"input":arg})
        try: trace[-1]["observation"]=execute(tool,arg)
        except Exception as exc: trace[-1]["error"]=str(exc)
    answer="；".join(f"{x['action']}: {x.get('observation',x.get('error'))}" for x in trace) or "无法规划安全动作"
    return {"answer":answer,"trace":trace,"stopped":len(plan(task))>max_steps}
def evaluate_trace(trace,required_tools=()):
    used={x.get("action") for x in trace}; errors=sum("error" in x for x in trace)
    return {"tool_coverage":len(used & set(required_tools))/max(1,len(required_tools)),"steps":len(trace),"errors":errors}
