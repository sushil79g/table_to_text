import yaml
from pathlib import Path

from haystack import Pipeline
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack_integrations.components.generators.ollama import OllamaGenerator

class GetAnswer():
    def __init__(self, document_store):
        self.pipeline = Pipeline()
        self.document_store = document_store

    def build_pipeline(self, retriver_prompt_location="template/retriver_prompt.yaml"):
        pathlocation = Path(retriver_prompt_location)
        with pathlocation.open("r") as stream:
            try:
                retriver_template = yaml.safe_load(stream)["retriver"].replace("\n", " ")
            except yaml.YAMLError as exc:
                raise exc
        self.pipeline.add_component("retriever", InMemoryBM25Retriever(document_store=self.document_store))
        self.pipeline.add_component("prompt_builder", PromptBuilder(template = retriver_template))
        self.pipeline.add_component("llm", OllamaGenerator(model="gemma3:4b", url="http://localhost:11434"))
        self.pipeline.connect("retriever", "prompt_builder.documents")
        self.pipeline.connect("prompt_builder", "llm")

    def predict_answer(self, question):
        response = self.pipeline.run({
            "prompt_builder": {"query": question},
            "retriever": {"query": question},
        })
        return response["llm"]["replies"]
