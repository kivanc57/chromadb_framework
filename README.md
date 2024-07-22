# Chroma Framework
## Overview
**Chroma Framework** is a Python-based application designed to manage and search text embeddings using a sentence transformer model. The framework enables users to create collections of text embeddings, add new documents, and query the closest texts based on input queries.

## Features
* **Embedding Management**: Create and manage collections of text embeddings.
* **Document Addtion**: Add new documents to the collection with metadata.
* **Text Search**: Find the closest texts to a given query using the embedding model.
* **Dynamic Path Handling**: Automatically determine file paths relative to the project directory.

## Installation
1. **Clone the repository**: 
    ```bash
    git clone https://github.com/yourusername/chromadb_framework
    ```

2. **Navigate to the project directory**:  
    ```bash
    cd chromadb_framework
    ```

3. **Install any required dependencies (if applicable)**.
    ```bash
    pip install -r requirements.txt
    ```

## Usage  
1. Ensure you have Python 3.x installed.

2. Run the application by executing:
    ```bash
    python main.py
    ```
3. Follow the on-screen prompts to manage embeddings and search texts.

## Project Structure

```markdown
📁 project-root
├── 📁 config
│ ├── 📄 __init__.py
│ └── 📄 constants.py
│
├── 📁 src
│ ├── 📄 __init__.py
│ ├── 📄 client.py
│ ├── 📄 collection.py
│ └── 📄 data.py
│
├── 📁 utils
│ ├── 📄 __init__.py
│ └── 📄 helpers.py
│
├── 📄 .gitignore
├── 📄 .gitattributes
└── 📄 main.py
```

* **config.py/**:  Contains configuration files.
  * ***\__init__.py***: Imports constants for model and collection configuration.
  * ***constants.py***: Defines constants used throughout the application.

* **src/**: Contains source code files.
  * ***\__init__.py***: Initializes the source package and sets up logging.
  * ***client.py***: Functions to create the database client.
  * ***collection.py***: unctions to manage collections and search texts.
  * ***data.py***: Functions to retrieve data from the specified folder.

* **utils/**: Contains utility Functions.
  * ***\__init__.py***: Imports helper functions.
  * ***helpers.py***: Utility functions for setting the model and getting paths.

* **.gitignore**: Specifies files and directories to be ignored by Git (e.g., virtual environments, build artifacts).
* **.gitattributes**: Ensures consistent line endings across different operating systems in the repository.
* **main.py**: The entry point of the application. Initializes settings, handles embedding operations, and manages text searches.

## Code Examples
### Main Program

```python
from config.constants import MODEL_NAME, COLLECTION_NAME, INPUT_QUERY
from src.client import get_client
from src.collection import get_or_create_collection, add_collection, find_closest_texts
from src.data import get_data
from utils.helpers import set_def_llm, get_path

def main():
    model_name = MODEL_NAME
    collection_name = COLLECTION_NAME
    input_query = INPUT_QUERY
    my_client = get_client()
    my_folder_path = get_path()
    embedding_function = set_def_llm(model_name)
    my_collection = get_or_create_collection(my_client, collection_name, embedding_function=embedding_function)
    my_documents, my_metadatas, my_ids = get_data(my_folder_path)
    add_collection(my_collection, my_documents, my_metadatas, my_ids)
    my_closest_texts = find_closest_texts(my_collection, input_query)
    print("Closest text(s):", my_closest_texts)

if __name__ == "__main__":
    main()

```

## Utility Functions
**helpers.py**: Utility functions for setting the model and getting paths.

```python
from os.path import abspath, dirname, join
from chromadb.utils import embedding_functions

def set_def_llm(model_name=None):
    try:
        if model_name:
            return embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
        else:
            return embedding_functions.DefaultEmbeddingFunction()
    except Exception as e:
        print(f"An error occurred while setting the sentence transformer.\n")
        return None

def get_path(folder_name="texts"):
    try:
        current_path = dirname(abspath(__file__))
        project_path = dirname(current_path)
        full_path = join(project_path, folder_name)
        return full_path
    except Exception as e:
        print(f"An error occurred while getting the folder path.\n")

```

## Client Creation
**client.py**: Functions to create the database client.
```python
from chromadb import PersistentClient

def get_client(path="vector_db"):
    try:
        client = PersistentClient(path=path)
        return client
    except FileNotFoundError:
        print(f"Database directory not found:")
    except Exception as e:
        print(f"An error occurred while creating the client: {e}")

```
## Collection Management
**collection.py**: Functions to manage collections and search texts.
```python
def get_or_create_collection(client, name, embedding_function):
    try:
        return client.get_or_create_collection(name=name, embedding_function=embedding_function)
    except Exception as e:
        print(f"An error occurred while creating the collection: {e}")

def add_collection(collection, documents, metadatas, ids):
    try:   
        collection.add(
            documents=documents, 
            metadatas=metadatas,
            ids=ids
            )
    except Exception as e:
        print(f"An error occurred while adding to the collection: {e}")

def find_closest_texts(collection, input_query, n_results=2):
    try:
        closest_text_names = list()
        results = collection.query(
            query_texts=[input_query],
            include=["metadatas"],
            n_results=n_results
        )
        for item in results["metadatas"][0]:
            closest_text_names.append(item["source"])
        return closest_text_names
    except Exception as e:
        print(f"An error occurred while finding the closest text: {e}")

```
## Data Preparation
**data.py**: Functions to retrieve data from the specified folder.

```python
from os import listdir
from os.path import join

def get_data(folder_path):
    try:
        documents = list()
        metadatas = list()
        ids = list()
        id_count = 1

        for file_name in listdir(folder_path):
            if file_name.endswith(".txt"):
                file_path = join(folder_path, file_name)
                id = "id" + str(id_count)
                with open(file_path) as file:
                    content = file.read()
                    documents.append(content)
                    metadatas.append({"source": file_name})
                    ids.append(id)
                id_count += 1
        return documents, metadatas, ids
    except Exception as e:
        print(f"An error occurred while creating the data: {e}")
        return [], [], []

```
## Contact
Let me know if there are any specific details you’d like to adjust or additional sections you want to include!  
* **Email**: kivancgordu@hotmail.com
* **Version**: 1.0.0
* **Date**: 22-06-2024

