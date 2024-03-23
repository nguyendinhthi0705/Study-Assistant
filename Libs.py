import os
from langchain.llms.bedrock import Bedrock
import boto3, json
from dotenv import load_dotenv
load_dotenv()

def call_claude_sonet(prompt):

    prompt_config = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                ],
            }
        ],
    }

    body = json.dumps(prompt_config)

    modelId = "anthropic.claude-3-sonnet-20240229-v1:0"
    accept = "application/json"
    contentType = "application/json"

    bedrock = boto3.client(service_name="bedrock-runtime")  
    response = bedrock.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )
    response_body = json.loads(response.get("body").read())

    results = response_body.get("content")[0].get("text")
    return results

def call_claude_sonet_stream(prompt):

    prompt_config = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                ],
            }
        ],
    }

    body = json.dumps(prompt_config)

    modelId = "anthropic.claude-3-sonnet-20240229-v1:0"
    accept = "application/json"
    contentType = "application/json"

    bedrock = boto3.client(service_name="bedrock-runtime")  
    response = bedrock.invoke_model_with_response_stream(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )

    stream = response['body']
    if stream:
        for event in stream:
            chunk = event.get('chunk')
            if chunk:
                 delta = json.loads(chunk.get('bytes').decode()).get("delta")
                 if delta:
                     yield delta.get("text")    
    
def rewrite_document(input_text): 
    prompt = """Your name is good writer. You need to rewrite content: 
        \n\nHuman: here is the content
        <text>""" + str(input_text) + """</text>
    \n\nAssistant: """
    return call_claude_sonet_stream(prompt)


def summary_stream(input_text):     
    prompt = f"""Based on the provided context, create summary the lecture
        \n\nHuman: here is the content
        <text>""" + str(input_text) + """</text>
    \n\nAssistant: """
    return call_claude_sonet_stream(prompt)

def query_document(question, docs): 
    prompt = """Human: here is the content:
        <text>""" + str(docs) + """</text>
        Question: """ + question + """ 
    \n\nAssistant: """

    return call_claude_sonet_stream(prompt)

def create_questions(input_text): 
    system_prompt = """You are an expert in creating high-quality multiple-choice quesitons and answer pairs 
    based on a given context. Based on the given context (e.g a passage, a paragraph, or a set of information), you should:
    1. Come up with thought-provoking multiple-choice questions that assess the reader's understanding of the context. 
    2. The questions should be clear and concise.
    3. The answer options should be logical and relevant to the context.

    The multiple-choice questions and answer pairs should be in a bulleted list: 
        1) Question: 

        A) Option 1

        B) Option 2 

        C) Option 3 

        Answer: A) Option 1 

         
    Continue with additional questions and answer pairs as needed.

    MAKE SURE TO INCLUDE THE FULL CORRECT ANSWER AT THE END, NO EXPLANATION NEEDED:"""
    
    prompt = f"""{system_prompt}. Based on the provided context, create 10 multiple-choice questions and answer pairs
        \n\nHuman: here is the content
        <text>""" + str(input_text) + """</text>
    \n\nAssistant: """
    return call_claude_sonet_stream(prompt)