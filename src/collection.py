#Get or create a collection with a given name
def get_or_create_collection(client, name, embedding_function):
    try:
        return client.get_or_create_collection(name=name, embedding_function=embedding_function)
    except Exception as e:
        print(f"An error occurred while creating the collection: {e}")

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

#Find the closest text(s) and return its name from includes. n_results is set to 1 by default.
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