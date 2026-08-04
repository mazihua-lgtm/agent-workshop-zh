# Agent Workshop ZH

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) [![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter)](https://jupyter.org/) [![pytest](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest)](https://pytest.org/)

> **企业 Agent 实战 1 天 workshop 素材**：用 5 个可运行 Lab，把 Prompt、结构化输出、工具调用、RAG 和 Agent Loop 串成一条工程化学习路径。

本仓面向已经了解 Python 与 LLM 基础、希望把模型接入业务流程的企业团队。它不是“从零认识大模型”的公开课，也不是一套生产系统；它提供可讲授、可修改、可测试的训练材料，帮助团队在一天内建立共同语言，并识别从 demo 到上线还缺少的安全、评测、权限和运维工作。

## 适用画像

- 正在评估客服、知识库、数据分析或内部助理场景的产品与研发团队；
- 需要统一 Prompt 与 Agent 工程规范的技术负责人；
- 已做过聊天 demo，但缺少结构化输出、工具白名单、引用和 guardrail 的交付团队；
- 希望用真实代码开展团队培训、架构讨论和 PoC 规划的接单客户。

参与者应能阅读基础 Python。所有默认示例离线运行，不提交、不要求真实 API key；如需比较 Claude / GPT，可由讲师在客户授权和预算范围内接入相同评测集。

## 快速开始

```bash
git clone https://github.com/mazihua-lgtm/agent-workshop-zh.git
cd agent-workshop-zh
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env                 # 可选：填入自己的 ANTHROPIC_API_KEY
jupyter lab                           # 依次打开 labs/01...05/notebook.ipynb
pytest -q                             # 一键验证 5 个 Lab
```

也可以在 IDE 中运行每个目录的 `notebook.py`。每个 Lab 同时包含中文主讲 Notebook、背景说明、5 道递进练习、参考答案和 pytest 自动测试，英文主要用于代码标识与必要术语。

## 路线图

| Lab | 主题 | 学完后能做什么 |
|---|---|---|
| 01 | Prompt Engineering | 把 zero-shot、few-shot 和步骤化推理写成可复用、可回归测试的 prompt contract；用同一数据集公平比较 Claude / GPT |
| 02 | Structured Output | 用 JSON Schema / Pydantic 思维约束字段、类型和错误，让 LLM 输出安全进入下游系统 |
| 03 | Tool Calling | 理解 function calling 的“模型提议、应用执行”边界，注册计算器、天气、只读查询并统一处理错误 |
| 04 | RAG | 实现分块、embedding、检索、带引用生成和无证据拒答，理解召回与幻觉之间的关系 |
| 05 | Agent Loop | 实现 ReAct / Plan-and-Execute 控制点，记录 trace，限制步数，加入工具白名单并评测覆盖率和错误率 |

完成后，参与者应能独立拆解一个 Agent PoC，定义输入输出契约，选择受控工具，构建最小 RAG，阅读执行轨迹，并为上线列出评测与 guardrail 清单。代码以标准库为主，故意保持可读；生产项目仍需替换模型、存储、鉴权、审计和可观测性组件。

## 一天怎么用

建议按 `docs/workshop_plan.md` 进行：上午建立 Prompt 与结构化契约，下午完成工具、RAG 与 Agent Loop；每个 Lab 采用“短讲解 → 代码演示 → 练习 → 测试复盘”。`docs/trainer_manual.md` 提供讲师准备、时间控制和常见问题，`docs/outcomes.md` 可用于培训验收。三个 `examples/customer_use_case_*.md` 是按业务模式脱敏的案例，不使用真实公司名、人员名或客户数据。

## 配套服务与计价参考

本仓是“团队培训”服务（**$1,200/次**）的公开 demo，便于客户在采购前审阅课程质量。内容可按企业技术栈、数据边界和案例定制为：

- **4 小时精简版：$1,200**，聚焦 2–3 个优先主题；
- **1 天标准版：$2,500**，覆盖 5 个 Lab 与 PoC 规划；
- **2 天 / 3 天内训：可定制**，增加客户场景工作坊、评测设计和架构评审。

价格仅作范围参考，最终以人数、准备工作、交付语言、现场/远程形式和数据合规要求为准；不承诺业务结果，也不以课程替代生产安全评审。

## 与其他项目的关系

本仓讲清通用机制，其他仓可作为 workshop 拓展 Lab：`pdf-rag-chatbot` 展示更完整的 PDF RAG 应用，`intentguard-pr-bot` 展示 Agent/LLM 在 PR 工作流中的意图与风险检查。它们不是本仓运行依赖，培训可按客户场景选择，不会把独立 demo 包装成单一生产产品。

## 开源承诺

**你不需要付费参加 workshop 才能使用这些内容。**全部 Notebook、练习、参考答案和测试均以 MIT License 开源，可自行学习、内部分享与修改。付费服务购买的是定制备课、讲师引导、现场答疑和团队场景讨论，而不是内容访问权。

欢迎通过 Issue 提交可复现的问题或课程改进建议。请勿在 Issue、Notebook 或 commit 中粘贴 API key、客户数据和内部文档。
