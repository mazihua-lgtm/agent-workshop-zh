# Lab 02 · Structured Output

## 目标

用 JSON Schema 定义接口契约，用 Pydantic 做生产校验；离线版本提供标准库校验器，安装 Pydantic 后可替换为 BaseModel。重点是拒绝不完整、类型错误和多余字段。

## 运行

```bash
cd labs/02_structured_output
python notebook.py
pytest -q test_lab.py
```

## 企业实践提醒

示例数据均为虚构训练数据；生产接入必须补充权限、日志、隐私与成本控制。
