from os import listdir
from os.path import join

#Prepare the data to insert to the collection
def get_data(folder_path):
    try:
        documents = list()
        metadatas = list()
        ids = list()
        id_count = 1

        for file_name in listdir(folder_path):
            #Checks whether file is in text format or not
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
