from pathlib import Path
from loguru import logger

from table_to_text import DataDescription, DataExtraction, GetAnswer, build_knowledge_base

def extract_data_from_doc():
    """Extracting data from knowledge base later used for retrival of question asked

    Returns:
        _type_: documnet_store object
    """
    file_location = Path("test data.csv")
    logger.info("Reading knowledge data from location: {}".format(file_location))
    extractor = DataExtraction()
    logger.info("Starting data extraction for preperation of knowledge base")
    extractor.table_extraction(file_location)
    description = DataDescription().load_description(extractor.columns, extractor.data)
    return description

def prepare_for_answer():
    """Building pipeline ready for answering question asked

    Returns:
        _type_: pipeline object
    """
    all_data = extract_data_from_doc()
    logger.info("Preparing knowledge base")
    doc_store = build_knowledge_base(all_data)
    logger.info("Preparing a answer retrival module")
    answer = GetAnswer(doc_store)
    logger.info("Preparing table question answering pipeline")
    answer.build_pipeline()
    return answer

def main():
    question = "What is the awareness score for Sony?"
    logger.info("Question to be asked: {}".format(question))
    answer_pipeline = prepare_for_answer()
    output = answer_pipeline.predict_answer(question)
    print(output)



if __name__ == "__main__":
    main()
