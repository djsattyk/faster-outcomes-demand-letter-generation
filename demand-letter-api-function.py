#imports
import base64
import json
from llamaapi import LlamaAPI


# Step 0: set up API endpoint and API key for Llama
llama = LlamaAPI("LL-b4NFuclPBqBsMcexa8uxM0Ld0ZbYzaN7ju074YzlkmUdbioBcsfYWmVp7fmP6E9u")

# Step 1: Read file
with open('DNL Auto Policy 20231028_PC_auto.pdf', 'rb') as file:
    pdf_data = file.read()

# Step 2: Convert file into readable format
# Choosing base64 string as conversion type (alternatively could use a byte stream)
encoded_pdf = base64.b64encode(pdf_data).decode('utf-8')
print(encoded_pdf)

# Step 3: create API function call
api_request_json = {
    "messages": [
        {"role": "user", "content": encoded_pdf}
    ],
    "functions": [
        {
            "name": "summarize_document",
            "description": "Summarize the content of the provided document",
            "parameters": {
                "type": "object",
                "properties": {
                    "document_base64": {
                        "type": "string",
                        "description": "Base64-encoded string of the PDF document"
                    }
                },
                "required": ["document_base64"]
            }
        }
    ],
    "function_call": "summarize_document"
}

response = llama.run(api_request_json)
print(json.dumps(response.json(), indent=2))
output = response.json()['choices'][0]['message']