# End-to-End RAG ChatBot

## This chatbot is created for chatting with pdf files leveraging open source LLM models like Mistrial using huggingface API and Pinecone for storing vectors of row text data as vector db.

## Stages for Development:

1. Data Ingestion: Leveraging Langchain, read PDF files and make them in chunks.
2. Store Embeddings: Creating embeddings of all chunks and indexing then storing them in a vector database, Here I used a cloud-based vector database which is Pinecone.
3. Retrievers: using cosine similarity search, retrieved relevant data as per user query.
4. Generate results: Passing all information with instructions prompt to the open source LLM model like Mistrial for generating appropriate results.


## Stack Used:  
- Python
- langchain
- Huggingface API
- Mistrial LLM
- Pinecone
- flask


1. Create conda environment
2. install requirments.txt file
3. create .env file and write pine cone and huggingface API
4. run store_index.py file for uploading embeddings in pinecone server
5. run app.py file
