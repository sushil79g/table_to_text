from table_to_text import DataDescription, DataExtraction
from pathlib import Path
from loguru import logger
def main():
    file_location = Path("test data.csv")
    extractor = DataExtraction()
    logger.info("Starting data extraction")
    extractor.table_extraction(file_location)
    logger.info("Starting LLM generation")
    description = DataDescription().load_description(extractor.columns, extractor.data)
    print(description)


if __name__ == "__main__":
    main()
