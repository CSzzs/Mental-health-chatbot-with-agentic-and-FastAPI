import os 
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI as LlamaOpenAI

llama_llm = LlamaOpenAI(model="gpt-40-mini", api_key=os.getenv("OPENAI_API_KEY"))


documents = SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(documents)

qurer_engine = index.as_query_engine(llm= llama_llm)

def query_documents(user_query:str) -> str:
    return str(qurer_engine.query(user_query))
