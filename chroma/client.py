from chromadb import PersistentClient

#Create the client
def get_client(path="vector_db"):
    try:
        client = PersistentClient(path=path)
        return client
    except FileNotFoundError:
        print(f"Database directory not found:")
    except Exception as e:
        print(f"An error occurred while creating the client: {e}")
