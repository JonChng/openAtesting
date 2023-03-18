import openai
import dotenv
import os
import requests

dotenv.load_dotenv()
apikey = os.environ['OPENAI_API']
org_key = os.environ['OPENAI_ORG_KEY']

endpoint1 = "https://api.openai.com/v1/completions"
endpoint2 = "https://api.openai.com/v1/models"
headers = {
    "Authorization": f"Bearer {apikey}",
    "Open-AI Organization":f"{org_key}",
    "Content-Type":"application/json"
}

prompt = input("What do you want to ask?")

params = {
    "model": "text-davinci-003",
    "prompt": f"{prompt}",
    "max_tokens": 300,
}


data = requests.post(endpoint1, json=params, headers=headers)
data.raise_for_status()


reply = data.json()['choices'][0]['text']

print(data.json())
print(reply)

# openai.organization = "org-W4ys9c0nnFmcXjAGaQ4JQ9Vy"
# openai.api_key = apikey
# openai.Model.list()






