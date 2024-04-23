    #Import the modules
    import chromadb
    import os

    #Construct the absolute path from the folder_path
    def get_relative_path(folder_path):
        current_dir = os.getcwd()
        return os.path.join(current_dir, folder_path)

    #Create the client
    def create_client(db_path=None):
        try:
            if db_path:
                chroma_client = chromadb.Client(db_path)
            else:
                chroma_client = chromadb.Client()
            return chroma_client
        except FileNotFoundError:
            print(f"Database directory not found:")
        except Exception as e:
            print(f"An error occurred while creating the client: {e}")
        
    #Get or create a collection with a given name
    def get_or_create_collection(client, collection_name):
        try:
            collection = client.get_or_create_collection(name=collection_name)
            return collection
        except Exception as e:
            print(f"An error occurred while creating the collection: {e}")

    #Prepare the data to insert to the collection
    def create_data(folder_path):
        try:
            documents = list()
            metadatas = list()
            ids = list()
            id_count = 1

            for file_name in os.listdir(folder_path):
                #Checks whether file is in text format or not
                if file_name.endswith(".txt"):
                    file_path = os.path.join(folder_path, file_name)
                    id = "id" + str(id_count)
                    with open(file_path) as file:
                        content = file.read()
                        documents.append(content)
                        metadatas.append({"source:": file_name})
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

    #Add the prepared data to the collection
    def add_collection(collection, documents, metadatas, ids):
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
            closest_text_name = result.includes[0]["source"]
            return closest_text_name
        except Exception as e:
            print(f"An error occurred while finding the closest text: {e}")


    def main():
        my_db_path = f"C:/Users/HP/Desktop"
        my_collection_name = f"my_collection"
        my_folder_path = f"texts"
        my_input_query = f"This is a text"

        my_relative_path = get_relative_path(my_folder_path)
        my_client = create_client()
        my_collection = get_or_create_collection(my_client, my_collection_name)
        my_documents, my_metadatas, my_ids = create_data(my_relative_path)
        add_collection(my_collection, my_documents, my_metadatas, my_ids)
        closest_text = find_closest_text(my_collection, my_input_query)
        print("Closest text:", closest_text)

    if __name__ == "__main__":
        main()
