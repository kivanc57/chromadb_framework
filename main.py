from config.constants import MODEL_NAME, COLLECTION_NAME, INPUT_QUERY
from chroma.client import get_client
from chroma.collection import get_or_create_collection, add_collection, find_closest_texts
from chroma.data import get_data
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
