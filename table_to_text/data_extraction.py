import yaml
import pandas as pd
from pathlib import Path
from loguru import logger

from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def load_llm():
    llm = OllamaLLM(model="gemma3:4b")
    return llm

class DataExtraction:
    def __init__(self):
        self.data = None
        self.columns = None

    def table_extraction(self, fileloc):
        if str(fileloc).endswith("csv"):
            self.data = pd.read_csv(fileloc, encoding="utf-8")
            self.columns = self.data.columns

        elif str(fileloc).endswith("xlsx"):
            self.data = pd.read_excel(fileloc)
            self.columns = self.data.columns
        else:
            raise ValueError("File must be .csv or .xlsx")


class DataDescription:
    def __init__(self):
        self.llm = load_llm()

    def load_description(self, column, data):
        location = Path("template/column_describe.yaml")
        with location.open("r") as stream:
            try:
                description_data = yaml.safe_load(stream)["prompt_describe"].replace("\n", " ")
            except yaml.YAMLError as exc:
                raise exc

        template = """
            You are a markettng and advertising focused data analyst. Given the following table:
            
            {data}
            
            And the descriptions:
            
            Columns:
            {column}
            
            whole data:
            {description_data}
            
            explain about the data and generate description for each and every brand looking at the data
            """
        prompt = PromptTemplate(
            input_variables=["data", "column", "description_data"],
            template=template
            )
        column = ", ".join(column.tolist())
        chain = LLMChain(llm=self.llm, prompt=prompt)
        table_str = data.to_string(index=False)
        logger.info("Table data type: {}".format(type(table_str)))
        logger.info("Table string {}".format(table_str))
        logger.info("column {}".format(column))
        logger.info("Description data {}".format(description_data))
        description = chain.run(
            data=table_str,
            column="\n".join(column),
            description_data="\n".join(description_data)
        )
        return description