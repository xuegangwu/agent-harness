# Agent Harness Engineer — 12 Week Milestones

> 目标：2026年7月，具备 Agent Harness Engineer 实战能力

---

## 🎯 Overall Milestones

| 阶段 | 时间 | 目标 | 交付物 |
|------|------|------|--------|
| **M0** | Week 0 | 环境就绪，GitHub 连接好 | 代码能跑，仓库在线 |
| **M1** | Week 1-4 | LangChain 精通 + RAG 实战 | 个人知识库 Demo |
| **M2** | Week 5-8 | Agent 架构 + 分布式组件 | Agent Harness Engine |
| **M3** | Week 9-12 | 生产级项目 + 求职准备 | GitHub Portfolio + 面试 Package |

---

## 📦 Milestone 1: LangChain + RAG 精通（Week 1-4）

### Week 1 — LangChain 基础 ✅
**目标：** 跑通 LangChain 三剑客（Chain / Memory / Tool）

| 天 | 任务 | 交付物 |
|----|------|--------|
| D1 | 环境搭建 + Quickstart | `w1d1_quickstart.py` ✅ |
| D2 | Prompt Template + Output Parser | 简历优化 Agent |
| D3 | LCEL 链式调用 | LCEL 重构版 |
| D4 | Memory 对话记忆 | 多轮对话 Bot |
| D5 | Tool 调用 | 带工具的助理 Agent |
| D6 | 整合 | CLI 聊天机器人项目 |
| D7 | 复盘 + 笔记 | 概念图 + Obsidian 笔记 |

**Week 1 交付：** `w1_cli_chatbot/`（完整可运行）

---

### Week 2 — LangChain 进阶
**目标：** Agent 深层原理 + LangSmith 调试

| 天 | 任务 | 交付物 |
|----|------|--------|
| D1 | ReAct / Plan-and-Execute 模式 | 模式对比文档 |
| D2 | Agent 类型深度（OpenAI / Conversational） | Agent 类型总结 |
| D3 | LangSmith 追踪调试 | Tracing 集成 |
| D4 | Tool Calling 高级（多工具并行、错误处理） | 鲁棒 Tool Agent |
| D5 | Callback 系统深度定制 | 自定义 Callback |
| D6 | 项目整合 | Agent CLI v2（带 Tools + Tracing） |
| D7 | 复盘 + W3 预习 | 笔记 + 问题清单 |

**Week 2 交付：** `w2_agent_cli/`（带 Tool Call + LangSmith Tracing）

---

### Week 3 — RAG 全链路
**目标：** 掌握 RAG 每一个环节，能独立搭建知识库

| 天 | 任务 | 交付物 |
|----|------|--------|
| D1 | Document Loading（PDF/TXT/Web） | 文档加载器 |
| D2 | Text Splitting（语义分块策略） | 分块对比实验 |
| D3 | Embedding + 向量数据库（Milvus/Qdrant） | 向量库集成 |
| D4 | Retrieval 策略（Top-K / MMR） | 检索优化 Demo |
| D5 | RAG 评估（RAGAs / Trulens） | 评估报告 |
| D6 | 整合：个人知识库 | RAG Pipeline 完整 Demo |
| D7 | 复盘 + 整理 | RAG 最佳实践文档 |

**Week 3 交付：** `w3_rag_knowledge_base/`（基于你自己内容的知识库）

---

### Week 4 — 向量数据库深度 + 项目整合
**目标：** 生产级 RAG + 第一阶段收尾

| 天 | 任务 | 交付物 |
|----|------|--------|
| D1 | Milvus 部署 + 运维 | Milvus 单机部署 |
| D2 | 向量索引优化（HNSW / IVF） | 索引对比实验 |
| D3 | 混合搜索（稀疏 + 密集） | 混合搜索实现 |
| D4 | RAG + Agent 结合 | Agent with RAG Knowledge |
| D5 | 第一阶段整合 | 统一 CLI 工具 |
| D6 | Portfolio 整理 | GitHub README 更新 |
| D7 | 复盘 + 第二阶段预习 | 学习总结 |

**Week 4 交付：** `w4_rag_agent/` + 完整 Portfolio README

---

## 📦 Milestone 2: Agent 架构 + 分布式（Week 5-8）

### Week 5 — Agent 设计模式
- ReAct / Plan-and-Execute / Supervised 三种模式深度理解
- 手动实现一个轻量状态机
- 对比 3 种模式的优劣场景

### Week 6 — State Machine / Graph Runtime
- 自己实现 Agent 调度核心（无 LangChain Agent）
- 理解状态机在 Agent 中的应用
- Graph Runtime 概念入门

### Week 7 — 多级记忆系统
- Short-term / Long-term / Episodic Memory 实现
- 记忆的压缩与检索策略
- 与 Vector DB 集成的长期记忆

### Week 8 — 分布式组件
- gRPC 入门 + Python 实现
- Redis 缓存策略
- Celery 异步任务队列
- 合并到 Agent Engine

**Week 8 交付：** `w8_agent_engine/`（可部署的 Agent 服务）

---

## 📦 Milestone 3: 出山 & 求职（Week 9-12）

### Week 9 — Agent Harness Engine 项目
- 整合 W5-W8 为一个完整的执行引擎
- 部署到 Cloudflare Workers 或 AWS EC2
- 完整的 README + 架构图

### Week 10 — 多模型路由 + Guardrail
- 实现 Model Routing（多 LLM 切换策略）
- Guardrail 安全护栏实现
- 成本与延迟优化

### Week 11 — 可观测性 + 性能
- Tracing 完整集成
- 性能测试与瓶颈分析
- 优化报告文档

### Week 12 — Portfolio + 求职激活
- LinkedIn 更新为 "AI Agent Engineer"
- Qiita 技术文章（用日语写）
- 猎头联系 + 模拟面试

**Week 12 交付：** 完整面试 Package

---

## 📊 Progress Tracking

```json
{
  "week0": { "status": "done", "date": "2026-04-06" },
  "week1": { "status": "pending", "date": "2026-04-07~04-13" },
  "week2": { "status": "pending", "date": "2026-04-14~04-20" },
  "week3": { "status": "pending", "date": "2026-04-21~04-27" },
  "week4": { "status": "pending", "date": "2026-04-28~05-04" },
  "week5": { "status": "pending", "date": "2026-05-05~05-11" },
  "week6": { "status": "pending", "date": "2026-05-12~05-18" },
  "week7": { "status": "pending", "date": "2026-05-19~05-25" },
  "week8": { "status": "pending", "date": "2026-05-26~06-01" },
  "week9": { "status": "pending", "date": "2026-06-02~06-08" },
  "week10": { "status": "pending", "date": "2026-06-09~06-15" },
  "week11": { "status": "pending", "date": "2026-06-16~06-22" },
  "week12": { "status": "pending", "date": "2026-06-23~06-29" }
}
```

---

## 🗓️ Week 1 详细日程（明天开始）

```
周一 D1  06:30 Quickstart 文档 + 环境验证
       晚  跑通 w1d1_quickstart.py

周二 D2  06:30 Prompt Template / Output Parser 文档
       晚  简历优化 Agent

周三 D3  06:30 LCEL 文档 + 流程图
       晚  LCEL 重构

周四 D4  06:30 Memory 文档
       晚  多轮对话 Bot

周五 D5  06:30 Tool 文档
       晚  带工具的助理 Agent

周六 D6  全天 CLI 聊天机器人整合

周日 D7  全天 复盘 + 笔记 + 概念图
```

---

## 📂 GitHub 仓库结构

```
agent-harness/
├── w1_cli_chatbot/         # Week 1 交付
├── w2_agent_cli/           # Week 2 交付
├── w3_rag_knowledge_base/  # Week 3 交付
├── w4_rag_agent/           # Week 4 交付
├── w5_agent_patterns/      # Week 5 交付
├── w6_state_machine/      # Week 6 交付
├── w7_memory_system/       # Week 7 交付
├── w8_agent_engine/        # Week 8 交付
├── w9_harness_engine/      # Week 9 交付
├── w10_router_guardrail/  # Week 10 交付
├── w11_observability/       # Week 11 交付
├── portfolio/              # Week 12 交付
├── docs/                   # 架构图 / 笔记
└── README.md               # 项目总览
```
