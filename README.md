# RAG tutorial with LangChain and LangServe

This tutorial helps you the build RAG models with LangChain and deploy them as a Fast API with LangServe




# Training and Serving machine learning with MLflow

## Install
* *pip install -r requirements* *

## Credentials
You need to create an .env file where you will put your Open API Key

## Start de LangServe serve with the following command

python app.py

## Multiple RAG

* *python client.py --rag-type "multiple_rag" --question "What is a TI-ADC ?"

## Fusion RAG

* *python client.py --rag-type "fusion_rag" --question "What is a TI-ADC ?"