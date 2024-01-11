from src.helper import load_pdf,download_hugging_face_embeddings,text_split
from langchain import HuggingFaceHub
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os


load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')


print("Data extratcting from pdf")

extract_data =load_pdf(r"D:\NLP_Project\ChatWithData_HuggingfaceAPI\Data")

print("text_slpits")

text_slpits = text_split(extract_data)


print("download embeddings")

embeddings = download_hugging_face_embeddings()

print("uploading embedding in Pinecone server")

pinecone.init(api_key=PINECONE_API_KEY,
              environment=PINECONE_API_ENV)

index_name="sqlchatbot"

#Creating Embeddings for Each of The Text Chunks & storing
docsearch=Pinecone.from_texts([t.page_content for t in text_slpits], embeddings, index_name=index_name)

print('Embeddings uploaded')


