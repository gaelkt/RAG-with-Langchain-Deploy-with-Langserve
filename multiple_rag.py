# from dataclasses import dataclass
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
import openai 
from dotenv import load_dotenv
from langchain.load import dumps, loads


load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

# database local path
CHROMA_PATH = "./chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def get_unique_union(documents: list[list]):
    """ Unique union of retrieved docs """
    # Flatten list of lists, and convert each Document to string
    flattened_docs = [dumps(doc) for sublist in documents for doc in sublist]
    # Get unique documents
    unique_docs = list(set(flattened_docs))
    # Return
    return [loads(doc) for doc in unique_docs]

def multiple_final_rag_chain():


    # Prepare the DB.
    embedding_function = OpenAIEmbeddings()
    vectorstore = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    retriever = vectorstore.as_retriever()
    
    
    
    # Multiple query different perspectives
    template = """You are an AI language model assistant. Your task is to generate five
different versions of the given user question to retrieve relevant documents from a vector
database. By generating multiple perspectives on the user question, your goal is to help
the user overcome some of the limitations of the distance-based similarity search.
Provide these alternative questions separated by newlines. Original question: {question}
    """
    
    prompt_perspectives = ChatPromptTemplate.from_template(template)
    
    from langchain_core.output_parsers import StrOutputParser
    
    llm_perspective = ChatOpenAI(temperature=0)

    generate_queries = (
    prompt_perspectives
    | llm_perspective
    | StrOutputParser()
    | (lambda x: x.split("\n"))
)
    
    retrieval_chain = generate_queries | retriever.map() | get_unique_union
    
    return retrieval_chain
    

