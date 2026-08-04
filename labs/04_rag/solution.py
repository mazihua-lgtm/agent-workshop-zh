import math, re
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List

@dataclass(frozen=True)
class Chunk:
    source: str
    text: str
    vector: Counter

def tokenize(text: str): return re.findall(r"[a-z0-9]+|[\u4e00-\u9fff]", text.lower())
def embed(text: str): return Counter(tokenize(text))
def chunk_text(text: str, chunk_size: int=120, overlap: int=20):
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size: raise ValueError("非法分块参数")
    return [text[i:i+chunk_size] for i in range(0,len(text),chunk_size-overlap) if text[i:i+chunk_size].strip()]
def cosine(a,b):
    dot=sum(v*b.get(k,0) for k,v in a.items()); na=math.sqrt(sum(v*v for v in a.values())); nb=math.sqrt(sum(v*v for v in b.values()))
    return dot/(na*nb) if na and nb else 0.0
def build_index(documents: Dict[str,str], chunk_size=120, overlap=20):
    return [Chunk(src,text,embed(text)) for src,body in documents.items() for text in chunk_text(body,chunk_size,overlap)]
def retrieve(query: str, index: List[Chunk], top_k=3):
    ranked=sorted(((cosine(embed(query),c.vector),c) for c in index), key=lambda x:x[0], reverse=True)
    return [(score,c) for score,c in ranked[:top_k] if score>0]
def answer(query: str, hits):
    if not hits: return "知识库中没有足够证据，无法回答。"
    evidence=" ".join(f"{c.text} [{c.source}]" for _,c in hits)
    return f"根据检索证据：{evidence}"
