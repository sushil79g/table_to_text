from haystack import Document
from haystack.document_stores.in_memory import InMemoryDocumentStore


def build_knowledge_base(all_data):
    document_store = InMemoryDocumentStore()
    all_data = all_data.split("\n\n")
    all_data = set(all_data)
    all_data = [Document(content=data) for data in all_data]
    document_store.write_documents(all_data)
    return document_store