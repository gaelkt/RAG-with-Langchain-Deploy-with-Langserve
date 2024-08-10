# RAG tutorial with LangChain and LangServe

This tutorial helps you the build RAG models with LangChain and deploy them as a Fast API with LangServe



## Install
* *pip install -r requirements* *

## Credentials
You need to create an .env file where you will put your Open API Key

## Start the LangServe serve with the following command

* *python app.py* *

## Multiple Query Retriever

* *python client.py --rag-type "multiple_rag" --question "What is a TI-ADC ?"* *

Distance-based vector database retrieval embeds (represents) queries in high-dimensional space and finds similar embedded documents based on "distance". But, retrieval may produce different results with subtle changes in query wording or if the embeddings do not capture the semantics of the data well. Prompt engineering / tuning is sometimes done to manually address these problems, but can be tedious.

The MultiQueryRetriever automates the process of prompt tuning by using an LLM to generate multiple queries from different perspectives for a given user input query. For each query, it retrieves a set of relevant documents and takes the unique union across all queries to get a larger set of potentially relevant documents. By generating multiple perspectives on the same question, the MultiQueryRetriever might be able to overcome some of the limitations of the distance-based retrieval and get a richer set of results.

## Fusion RAG

It performs multiple query generation and Reciprocal Rank Fusion to re-rank search results and generate a more relevant context.

* *python client.py --rag-type "fusion_rag" --question "What is a TI-ADC ?" * *


## Query decomposition
This process of splitting an input into multiple distinct sub-queries is what we refer to as query decomposition. It is also sometimes referred to as sub-query generation

https://arxiv.org/pdf/2205.10625

Coming ...

## Step back prompting

Step-Back Prompting is a prompting technique enabling LLMs to perform abstractions, derive high-level concepts & first principles from which accurate answers can be derived.

Coming ...

https://arxiv.org/pdf/2310.06117.pdf