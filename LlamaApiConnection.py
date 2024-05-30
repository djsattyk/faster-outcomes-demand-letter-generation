import json
from llamaapi import LlamaAPI
import PyPDF2
from openai import OpenAI, OpenAIError

# Function using, PyPDF2, to convert PDF to text
def extract_text_from_pdf(pdf_path):
    reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text

'''
This used to be file paths but now trying google drive.
'''
# List of files to convert
file_list = ["https://drive.google.com/file/d/1MwpkMCo_LTf-NUKwJTdXPxWRSK66c5vW/view?usp=sharing",
              "https://drive.google.com/file/d/1eqQWykpIuam8m4RVoP6Ve45PDw_cKAqI/view?usp=sharing",
              "https://drive.google.com/file/d/1Wok2L1WW8Q5R53hFAxO3WIpFDqZuMWKD/view?usp=sharing"]

file_list = ["Ex. 2 - Rental Agreement (v2).pdf",
              "Ex. 1 - Insurance Policy.pdf",
              "Matter Summary.pdf"]


#####################################################################################
########## THIS MAKES THE PROMPT HAVE TOO MUCH TEXT TO HANDLE #######################
#####################################################################################
# empty list of pdfs turned into text
# text_file_list =[]
# # convert all files to text
# for i, file_ in enumerate(file_list):
#     pdf_text = extract_text_from_pdf(file_)
#     text_file_list.append(f"Information from PDF {i+1}:\n\n{pdf_text}")
#####################################################################################
#####################################################################################
#####################################################################################


# create a prompt section for each pdf link
prompt_sections = []
for i, link in enumerate(file_list):
    prompt_sections.append(f"Please refer to the information in PDF {i+1}: {link}")


client = OpenAI(
  api_key = "LL-b4NFuclPBqBsMcexa8uxM0Ld0ZbYzaN7ju074YzlkmUdbioBcsfYWmVp7fmP6E9u",
  base_url = "https://api.llama-api.com"
)

final_prompt = "Write me a demand letter. Here is the relevant information from the PDFs:\n\n" + "\n\n".join(prompt_sections)

try:
  response = client.chat.completions.create(
      model="llama-13b-chat",
      messages=[
          {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
          {"role": "user", "content": final_prompt}
      ]
  )
except OpenAIError as e:
    print(f"OpenAI API error: {e}")
    

#print(response)
# print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)