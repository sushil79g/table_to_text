<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">


<em>Unlock insights. Transform data into actionable answers.</em>

<!-- BADGES -->
<!-- local repository, no metadata badges. -->

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/TOML-9C4121.svg?style=default&logo=TOML&logoColor=white" alt="TOML">
<img src="https://img.shields.io/badge/LangChain-1C3C3C.svg?style=default&logo=LangChain&logoColor=white" alt="LangChain">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/pandas-150458.svg?style=default&logo=pandas&logoColor=white" alt="pandas">
<img src="https://img.shields.io/badge/uv-DE5FE9.svg?style=default&logo=uv&logoColor=white" alt="uv">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=default&logo=YAML&logoColor=white" alt="YAML">

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

Unlock the power of your structured data with Source Code Summaries, a developer tool that transforms tabular data into actionable insights and enables intelligent question answering.

**Why Source Code Summaries?**

This project simplifies the creation of knowledge bases from tabular data, enabling developers to build intelligent question-answering systems and generate descriptive insights from raw data. The core features include:

- 🔵 **Automated Data Description:** Leverages large language models to generate descriptive insights from CSV and XLSX files, tailored for marketing and advertising applications.
- 🟠 **Question-Answering Pipeline:** Orchestrates a robust pipeline to process data, build a document store, and predict answers to user-specified questions.
- 🟣 **Knowledge Base Construction:** Transforms raw text blocks into a structured format, enabling efficient indexing and querying for search and retrieval functionalities.
- <0xF0><0x9F><0xA9><0xBB> **Retrieval-Augmented Generation (RAG):**  Utilizes a document store and language model to formulate responses to user questions, ensuring contextually relevant and accurate answers.
- <0xF0><0x9F><0x9F><0xAA> **Standardized YAML Configuration:** Defines prompts and key brand metrics, ensuring consistency and clarity across the project.

---

## Features

|     | Component      | Details                             |
| :--- | :-------------- | :----------------------------------- |
| ⚙️ | **Architecture** | <ul><li>Python-centric.</li><li>Microservice architecture (given dependencies like `uv`).</li><li>Event-driven components possible.</li><li>uses a retrieval-augmented generation (RAG) pattern.</li></ul> |
| 🔩 | **Code Quality** | <ul><li>Uses `pyproject.toml` - Using a modern Python packaging/linting setup (UV).</li><li>YAML configuration files (`retriver_prompt.yaml`, `column_describe.yaml`) suggest structured configuration.</li><li>`loguru` indicates robust logging practices.</li></ul> |
| 🔌 | **Integrations** | <ul><li>**Langchain:** Core integration for LLM workflows.</li><li>**Langchain-Ollama:**  Connects to Ollama for local LLM serving.</li><li>**Haystack-AI:**  Used for building search pipelines.</li><li>**Ollama-Haystack:** Combines Haystack and Ollama.</li><li>**Pandas:** Data manipulation and analysis.</li><li>**YAML/TOML:** Configuration file parsing.</li></ul> |
| 🧩 | **Modularity**   | <ul><li>Modular design.</li><li>YAML configuration files promote modularity.</li><li>Langchain's modular components utilized.</li><li>Potential for plugin architecture.</li></ul> |
| 🧪 | **Testing**      | <ul><li>`pyproject.toml` Contains testing framework configuration (e.g., pytest).</li><li>Requires investigation of test suite coverage and quality.</li><li>Integration tests are crucial given the number of dependencies.</li></ul> |
| ⚡️ | **Performance**  | <ul><li>Ollama suggests local LLM inference for potentially faster response times.</li><li>Haystack's indexing and retrieval pipelines impact performance.</li><li>Profiling and optimization likely needed for complex workflows.</li></ul> |
| 🛡️ | **Security**     | <ul><li>Requires review of dependency vulnerabilities (using tools like `pip-audit`).</li><li>Sensitive data handling (API keys, credentials) needs careful consideration.</li><li>Input validation is critical to prevent prompt injection attacks.</li></ul> |

---

## Project Structure

```sh
└── /
    ├── LICENSE
    ├── main.py
    ├── pyproject.toml
    ├── README.md
    ├── table_to_text
    │   ├── __init__.py
    │   ├── data_extraction.py
    │   ├── get_answer.py
    │   └── knowledge_base.py
    ├── template
    │   ├── column_describe.yaml
    │   └── retriver_prompt.yaml
    └── uv.lock
```

### Project Index

<details open>
    <summary><b><code>/</code></b></summary>
    <!-- __root__ Submodule -->
    <details>
        <summary><b>__root__</b></summary>
        <blockquote>
            <div class='directory-path' style='padding: 8px 0; color: #666;'>
                <code><b>⦿ __root__</b></code>
            <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #f8f9fa;'>
                    <th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
                    <th style='text-align: left; padding: 8px;'>Summary</th>
                </tr>
            </thead>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='/LICENSE'>LICENSE</a></b></td>
                    <td style='padding: 8px;'>- License grants broad usage rights for the entire project, ensuring open access and modification capabilities for developers and collaborators<br>- It clearly outlines the conditions under which the software and associated documentation can be used, distributed, and adapted, while also limiting liability for the original author.</td>
                </tr>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='/main.py'>main.py</a></b></td>
                    <td style='padding: 8px;'>- A question-answering pipeline processes data extracted from a knowledge base<br>- It reads tabular data from a CSV file, builds a document store, and then utilizes this store to predict and output an answer to a user-specified question<br>- The entire process prepares a system capable of retrieving answers from structured data.</td>
                </tr>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='/pyproject.toml'>pyproject.toml</a></b></td>
                    <td style='padding: 8px;'>- Configuration for the table-to-text project is defined within pyproject.toml<br>- It declares project metadata, specifies versioning details, and outlines essential dependencies including Haystack-AI, Langchain, and Ollama-Haystack<br>- Ultimately, this file ensures consistent project setup and facilitates reproducible builds by managing external libraries required for table data conversion to text.</td>
                </tr>
            </table>
        </blockquote>
    </details>
    <!-- table_to_text Submodule -->
    <details>
        <summary><b>table_to_text</b></summary>
        <blockquote>
            <div class='directory-path' style='padding: 8px 0; color: #666;'>
                <code><b>⦿ table_to_text</b></code>
            <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #f8f9fa;'>
                    <th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
                    <th style='text-align: left; padding: 8px;'>Summary</th>
                </tr>
            </thead>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='/table_to_text/data_extraction.py'>data_extraction.py</a></b></td>
                    <td style='padding: 8px;'>- Data extraction and description functionality resides within <code>data_extraction.py</code><br>- It handles loading tabular data from CSV or XLSX files and then leverages a large language model to generate descriptive insights about the data, specifically tailored for marketing and advertising applications<br>- This component acts as a bridge between raw data and actionable intelligence within the broader project.</td>
                </tr>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='/table_to_text/get_answer.py'>get_answer.py</a></b></td>
                    <td style='padding: 8px;'>- Answer generation functionality resides within <code>get_answer.py</code>, orchestrating a retrieval-augmented generation pipeline<br>- It leverages a document store to retrieve relevant information and then uses a language model to formulate responses to user questions<br>- This component acts as the primary interface for querying the knowledge base and obtaining answers based on the indexed documents.</td>
                </tr>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='/table_to_text/knowledge_base.py'>knowledge_base.py</a></b></td>
                    <td style='padding: 8px;'>- Knowledge base construction is handled within <code>knowledge_base.py</code>, a crucial component for ingesting textual data into the system<br>- It transforms raw text blocks, extracted from various sources, into a structured format suitable for indexing and querying<br>- This process prepares the data for use by other modules, enabling search and retrieval functionalities across the entire application.</td>
                </tr>
            </table>
        </blockquote>
    </details>
    <!-- template Submodule -->
    <details>
        <summary><b>template</b></summary>
        <blockquote>
            <div class='directory-path' style='padding: 8px 0; color: #666;'>
                <code><b>⦿ template</b></code>
            <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #f8f9fa;'>
                    <th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
                    <th style='text-align: left; padding: 8px;'>Summary</th>
                </tr>
            </thead>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='/template/column_describe.yaml'>column_describe.yaml</a></b></td>
                    <td style='padding: 8px;'>- Descriptions for key brand metrics are defined within this configuration<br>- It serves to standardize and document the meaning of important performance indicators used throughout the project, ensuring consistent understanding and application when analyzing brand health and marketing campaign effectiveness<br>- These definitions facilitate clear communication and reliable data interpretation across teams.</td>
                </tr>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='/template/retriver_prompt.yaml'>retriver_prompt.yaml</a></b></td>
                    <td style='padding: 8px;'>- Prompt generation for question answering relies on this YAML configuration<br>- It defines the structure of prompts fed to a language model, incorporating provided context documents<br>- Effectively, it dictates how relevant information is presented to the model to facilitate accurate and grounded responses to user queries within the overall knowledge retrieval system.</td>
                </tr>
            </table>
        </blockquote>
    </details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Uv

### Installation

Build  from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/sushil79g/table_to_text.git
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd table_to_text
    ```

3. **Install the dependencies:**

    **Using [uv](https://docs.astral.sh/uv/):**

    ```sh
    ❯ uv sync --all-extras --dev
    ```

### Usage

Run the project with:

**Using [uv](https://docs.astral.sh/uv/):**
```sh
uv run python main.py
```

### Testing

 uses the {__test_framework__} test framework. Run the test suite with:

**Using [uv](https://docs.astral.sh/uv/):**
```sh
uv run pytest tests/
```

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement table explaination</strike>
- [X] **`Task 2`**: <strike>Implement question answering on tabular data.</strike>
- [ ] **`Task 3`**: combine tabular with other unstructure data.

---



## License

 is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
