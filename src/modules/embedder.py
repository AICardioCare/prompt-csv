import os
import pickle
import tempfile
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings


class Embedder:
    def __init__(self):
        self.PATH = "embeddings"
        self.createEmbeddingsDir()

    def createEmbeddingsDir(self):
        """
        Creates a directory to store the embeddings vectors
        """
        if not os.path.exists(self.PATH):
            os.mkdir(self.PATH)

    def storeDocEmbeds(self, file, original_filename):
        """
        Stores document embeddings using Langchain and FAISS
        """
        with tempfile.NamedTemporaryFile(mode="wb", delete=False) as tmp_file:
            tmp_file.write(file)
            tmp_file_path = tmp_file.name

        loader = CSVLoader(
            file_path=tmp_file_path,
            encoding="utf-8",
            csv_args={
                "delimiter": ",",
            },
        )
        data = loader.load()

        embeddings = OpenAIEmbeddings()

        vectors = FAISS.from_documents(data, embeddings)
        os.remove(tmp_file_path)

        # Save the vectors to a pickle file
        with open(f"{self.PATH}/{original_filename}.pkl", "wb") as f:
            pickle.dump(vectors, f)

    def getDocEmbeds(self, file, original_filename):
        """
        Retrieves document embeddings
        """
        if not os.path.isfile(f"{self.PATH}/{original_filename}.pkl"):
            self.storeDocEmbeds(file, original_filename)

        # Load the vectors from the pickle file
        with open(f"{self.PATH}/{original_filename}.pkl", "rb") as f:
            vectors = pickle.load(f)

        return vectors
