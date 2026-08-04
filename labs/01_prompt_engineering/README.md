# Lab 01 · Prompt Engineering

## 目标

把 prompt 当作可测试的软件接口：明确角色、任务、约束、示例与输出格式，并比较 zero-shot、few-shot 与显式推理步骤。Claude / GPT 的差异应通过同一评测集实测，而不是凭印象下结论。

## 运行

```bash
cd labs/01_prompt_engineering
python notebook.py
pytest -q test_lab.py
```

## 企业实践提醒

示例数据均为虚构训练数据；生产接入必须补充权限、日志、隐私与成本控制。
