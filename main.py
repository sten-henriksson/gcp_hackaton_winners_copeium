from litellm import completion
import json 


# https://console.developers.google.com/apis/api/aiplatform.googleapis.com/overview?project=my-project-1732217065701
#  https://console.developers.google.com/apis/api/aiplatform.googleapis.com/overview?project=my-project-1732217065701

response = completion(
  model="vertex_ai/gemini-2.5-flash-preview-05-20",
  messages=[{"content": "You are a good bot.","role": "system"}, {"content": "Hello, how are you?","role": "user"}], 
)
print(response)
