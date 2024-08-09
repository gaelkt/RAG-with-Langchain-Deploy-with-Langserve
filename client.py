import requests
import argparse



parser = argparse.ArgumentParser()

# Input of the query
parser.add_argument("--rag_type", choices=['multiple_rag', 'fusion_rag'], default = "multiple_rag", help="select type of rag")
parser.add_argument("--question", help="Enter your question")

args = parser.parse_args()
rag_type = args.rag_type
question = args.question

response=requests.post(
    "http://localhost:8000/" + rag_type + "/invoke",
    json={'input':{'question':question}})

print(response.json()['output'])
