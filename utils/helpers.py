#Import the modules
from os.path import abspath, dirname, join
from chromadb.utils import embedding_functions

#Change the LLM if requested
def set_def_llm(model_name=None):
    try:
        if model_name:
            return embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
        else:
            return embedding_functions.DefaultEmbeddingFunction()
    except Exception as e:
        print(f"An error occurred while setting the sentence transformer.\n")
        return None

#Merge the given directory with the given file path
def get_path(folder_name="texts"):
    try:
        current_path = dirname(abspath(__file__))
        project_path = dirname(current_path)
        full_path = join(project_path, folder_name)
        return full_path
    except Exception as e:
        print(f"An error occurred while getting the folder path.\n")
