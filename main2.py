from litellm import completion
import json 

## GET CREDENTIALS 
## RUN ## 
# !gcloud auth application-default login - run this to add vertex credentials to your env
## OR ## 
file_path = 'my-project-1732217065701-67944e3b12c4.json'

# Load the JSON file
with open(file_path, 'r') as file:
    vertex_credentials = json.load(file)

# Convert to JSON string
vertex_credentials_json = json.dumps(vertex_credentials)

## COMPLETION CALL 
response = completion(

  model="vertex_ai/gemini-2.5-flash-preview-05-20",

  messages=[{ "content": "Hello, how are you?","role": "user"}],
  vertex_credentials=vertex_credentials_json
)
print(response)
