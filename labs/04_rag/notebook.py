# %% [markdown]
# # Lab 04 · RAG
# 从分块、稀疏 embedding、余弦检索到带引用回答，完整走通教学版 RAG。这里刻意不用向量数据库，便于看清机制；生产环境可替换 embedding 和存储层。
# %%
from solution import build_index, retrieve, answer

docs={"security.md":"所有生产访问必须启用 MFA。密钥每 90 天轮换。","support.md":"企业客户支持时间为工作日 9:00-18:00。"}
index=build_index(docs, chunk_size=24, overlap=4)
hits=retrieve("生产访问要启用什么？", index, top_k=2)
print(hits)
print(answer("生产访问要启用什么？", hits))
