from haystack import Pipeline ## for ccreating haystack pipeline
from haystack.components.writers import DocumentWriter ## for vector database
from haystack.components.preprocessors import DocumentSplitter ## for splitting thetext documents
from haystack.components.embedders import SentenceTransformersDocumentEmbedder ## for converting text into word vector embeddings
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument ## converting pdf file into normal text file
from pathlib import Path
import os
from dotenv import load_dotenv
from QASystem.utils import pinecone_config


## creating a python fucntion which will take pinecone vector database as the input
## and in retrun we will be getting vector embeddings of our text data stored in the provided vector database
## all the process converting text into pdf,splitting the text into chunks
## converting these chunks into word vector embeddings and storing these all the word vector embeddings into 
## the given vector database will happening in the given function


def ingest(document_store): ## document_store--> a pinecone vector database
    ## let us creating the haystack pipeline for data ingestion part 
    ## which is the most important part in RAG pipeline

    indexing = Pipeline()
    ## creating all the required components for the RAG pipeline
    indexing.add_component("converter",PyPDFToDocument()) ## for converting pdf into document
    indexing.add_component("splitter",DocumentSplitter(split_by="sentence",split_length = 2)) ## for splitting the text into chunks
    indexing.add_component("embedder",SentenceTransformersDocumentEmbedder()) ## for generating wordvector embeddings of text chunk
    indexing.add_component("writer",DocumentWriter(document_store)) ## for storing the word vector embeddings into vector database

    ## connecting all the components of the pipeline
    indexing.connect("converter","splitter") 
    indexing.connect("splitter","embedder")
    indexing.connect("embedder","writer")
    ## storing the data as embedding in the pinecone vector database
    indexing.run({"converter":{"sources":[Path("C:\\Users\\rajpu\\rag_with_haystack3\\data")]}})
if __name__ == "__main__":
    document_store = pinecone_config()
    ingest(document_store)
