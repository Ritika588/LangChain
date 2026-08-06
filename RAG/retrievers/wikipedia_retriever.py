import os

os.environ["OPENAI_API_KEY"] = "....."
from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=3, lang='en')

query = "the geopolitical history of india and pakistan from the perspective of a chinese"
docs = retriever.invoke(query)

docs
for i, doc in enumerate(docs):
    print(f"-----Result{i+1}-----")
    print(f"Content{doc.page_content}")