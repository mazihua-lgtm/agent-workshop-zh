# Lab 04 · RAG

## 目标

从分块、稀疏 embedding、余弦检索到带引用回答，完整走通教学版 RAG。这里刻意不用向量数据库，便于看清机制；生产环境可替换 embedding 和存储层。

## 运行

```bash
cd labs/04_rag
python notebook.py
pytest -q test_lab.py
```

## 企业实践提醒

示例数据均为虚构训练数据；生产接入必须补充权限、日志、隐私与成本控制。
