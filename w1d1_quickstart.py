#!/usr/bin/env python3
"""
W1D1 - LangChain Quickstart 测试
验证环境 + API Key 是否正常工作
"""

import os
from dotenv import load_dotenv

# 加载 .env 文件（创建 .env 后填入 Key）
load_dotenv()

api_key = os.getenv("CURRENT_API_KEY")
api_base = os.getenv("CURRENT_API_BASE")
model = os.getenv("CURRENT_MODEL", "moonshot-v1-8k")

if not api_key or api_key == "填入你的Kimi API Key":
    print("❌ 还没配置 API Key！")
    print("1. 复制 .env.example 为 .env")
    print("2. 填入你的 Kimi API Key")
    print("3. 获取地址: https://platform.moonshot.cn/")
    exit(1)

print(f"✅ 配置检查:")
print(f"   API Base: {api_base}")
print(f"   Model: {model}")
print(f"   API Key: {api_key[:8]}...{api_key[-4:]}")
print()

# ===== 1. 第一个例子：LLM 调用 =====
print("🔵 测试 1: LLM 调用")
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model=model,
    api_key=api_key,
    base_url=api_base,
    temperature=0.7,
)

response = llm.invoke("用一句话解释 LangChain 是什么？")
print(f"   回复: {response.content}")
print()

# ===== 2. 第二个例子：Prompt Template =====
print("🔵 测试 2: Prompt Template")
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的{language}翻译专家"),
    ("human", "把下面这句话翻译成{language}：{sentence}")
])

chain = prompt | llm
response = chain.invoke({
    "language": "日语",
    "sentence": "Agent Harness is the infrastructure for controlling AI agents"
})

print(f"   回复: {response.content}")
print()

# ===== 3. 第三个例子：带输出的结构化 =====
print("🔵 测试 3: 结构化输出")
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

output_parser = StrOutputParser()

chain = (
    PromptTemplate.from_template("讲一个关于{name}的冷笑话，最多50字")
    | llm
    | output_parser
)

response = chain.invoke({"name": "程序员"})
print(f"   回复: {response}")
print()

print("=" * 50)
print("🎉 全部测试通过！W1D1 环境搭建成功！")
print("=" * 50)
