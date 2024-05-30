

import requests
import json
from llamaapi import LlamaAPI

# Initialize the SDK
api_token = "LL-b4NFuclPBqBsMcexa8uxM0Ld0ZbYzaN7ju074YzlkmUdbioBcsfYWmVp7fmP6E9u"
llama = LlamaAPI(api_token)

# Send the prompt to the API
prompt = "create a demand letter"
response = llama.complete(prompt)

# Extract the output from the response
output = response['text']  # Adjust according to the actual response structure

print(output)