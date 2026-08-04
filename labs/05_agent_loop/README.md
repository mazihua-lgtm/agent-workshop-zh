# Lab 05 · Agent Loop

## 目标

实现一个可观察、可限制、可评测的 Agent Loop：规划动作、执行白名单工具、记录 observation，并通过最大步数与敏感操作 guardrail 防止失控。对比 ReAct 与 Plan-and-Execute 的控制点。

## 运行

```bash
cd labs/05_agent_loop
python notebook.py
pytest -q test_lab.py
```

## 企业实践提醒

示例数据均为虚构训练数据；生产接入必须补充权限、日志、隐私与成本控制。
