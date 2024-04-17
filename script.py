import chromadb
import os

#Create the client
def create_client(db_path):
    try:
        chroma_client = chromadb.Client(path=db_path)
        return chroma_client
    except FileNotFoundError:
        print(f"Database directory not found: {db_path}")
    except Exception as e:
        print(f"An error occurred while creating the client: {e}")
    
#Create a collection with a given name
def create_collection(client, collection_name):
    try:
        collection = client.create_collection(name=collection_name)
        return collection
    except Exception as e:
        print(f"An error occurred while creating the collection: {e}")

#Prepare the data to insert to the collection
def create_data(path):
    try:
        documents = list()
        metadatas = list()
        ids = list()
        id_count = 1

        for file_name in os.listdir():
            #Checks whether file is in text format or not
            if file_name.endswith(".txt"):
                file_path = os.path.join(path, file_name)
                id = "id" + str(id_count)
                with open(file_path) as file:
                    content = file.read()
                    documents.append(content)
                    metadatas.append({"source: " + file_name})
                    ids.append(id)
                id_count += 1
    except Exception as e:
        print(f"An error occurred while creating the data: {e}")
    finally:
        return documents, metadatas, ids
    """
    Generating embeddings automatically after
    adding the documents, metadatas as file_name and, ids
    """
def add_collection(collection, documents, metadatas, ids): #Add the prepared data to the collection
    try:
        collection.add(
            documents=documents, 
            metadatas=metadatas,
            ids=ids
            )
    except Exception as e:
        print(f"An error occurred while adding to the collection: {e}")

#Find the closest text and return its name from includes
def find_closest_text(collection, input_query):
    try:
        result = collection.query(
            query_texts=[input_query],
            includes = ["source"],
            n_results=1
        )
        return result.includes
    except Exception as e:
        print(f"An error occurred while finding the closest text: {e}")


def main():
    my_db_path = f"C:/Users/HP/Desktop"
    my_collection_name = f"my_collection"
    my_path = f"C:/Users/HP/Desktop/texts"
    my_input_query = f"This is a text"

    my_client = create_client(my_db_path)
    my_collection = create_collection(my_client, my_collection_name)
    documents, metadatas, ids = create_data(my_path)
    add_collection(my_collection, documents, metadatas, ids)
    closest_text = find_closest_text(my_collection, my_input_query)
    print("Closest text:", closest_text)

if __name__ == "__main__":
    main()