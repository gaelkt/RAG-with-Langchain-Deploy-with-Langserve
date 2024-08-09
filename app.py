from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
import openai 

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']




from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from multiple_rag import multiple_final_rag_chain
from fusion_rag import rag_fusion_final_rag_chain




app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)




# Multiple queries

# Simple RAG
template = """Answer the following question based on this context:

            {context}

                Question: {question}
                """

prompt_multiple = ChatPromptTemplate.from_template(template)

model_multiple = ChatOpenAI(temperature=0)
retrieval_chain = multiple_final_rag_chain()

final_rag_chain = (
    {"context": retrieval_chain,
     "question": itemgetter("question")}
    | prompt_multiple
    | model_multiple
    | StrOutputParser()
)

add_routes(
    app,
    final_rag_chain,
    path="/multiple_rag",
)

# RAG Fusion
template = """Answer the following question based on this context:

            {context}

                Question: {question}
                """

prompt_rag_fusion = ChatPromptTemplate.from_template(template)

model_rag_fusion = ChatOpenAI(temperature=0)
retrieval_rag_fusion = rag_fusion_final_rag_chain()

final_rag_fusion = (
    {"context": retrieval_rag_fusion,
     "question": itemgetter("question")}
    | prompt_rag_fusion
    | model_rag_fusion
    | StrOutputParser()
)

add_routes(
    app,
    final_rag_fusion,
    path="/fusion_rag",
)




if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)