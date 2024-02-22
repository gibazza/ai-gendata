import json
import os

from dotenv import load_dotenv
from openai import AzureOpenAI
from prompts.prompts import SYSTEM_MESSAGE

load_dotenv()

def get_completion_from_messages(system_message, user_message, temperature, max_tokens, model=os.environ["OPENAI_DEPLOYMENT_NAME"]) -> str:

    client = AzureOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        api_version="2024-02-15-preview"
    )
    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    # Schema representation
    with open('./schema/person_schema.json',"r") as json_object: 
        schema_json = json.load(json_object)
        schemas = json.dumps(schema_json, indent=2)
    #print (schemas)

    # Format the system message with the schema
    formatted_system_message = SYSTEM_MESSAGE.format(schema=schemas)
    #print (formatted_system_message)

    user_question = "Generate 10 users please."
    response = get_completion_from_messages(formatted_system_message, user_question,1,8000)
    #Load to a dictionary
    json_dict = json.loads(response)
    #Nicely format the JSON output
    json_response = json.dumps(json_dict, indent=2)
    print(f"{json_response}")