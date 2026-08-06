from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader('cricket.txt', encoding="utf-8")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 150,
    chunk_overlap = 30,
    separator = ''
)

result = splitter.split_documents(docs)

for i, doc in enumerate(result):
    print(f"Chunk {i+1}")
    print(doc.page_content)
    print("-" * 50)