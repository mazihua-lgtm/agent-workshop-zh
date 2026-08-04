# Lab 03 · Tool Calling

## 目标

Function calling 不是让模型直接执行代码，而是让模型产生受约束的调用意图，再由应用完成白名单校验、执行和错误封装。本 Lab 注册计算器、天气和只读数据库三个工具。

## 运行

```bash
cd labs/03_tool_calling
python notebook.py
pytest -q test_lab.py
```

## 企业实践提醒

示例数据均为虚构训练数据；生产接入必须补充权限、日志、隐私与成本控制。
