from litellm import completion
from smolagents import CodeAgent,LiteLLMModel 
import json 
import os
    
os.environ["OPENROUTER_API_KEY"] = os.getenv('OPENROUTER_API_KEY')
model = LiteLLMModel("openrouter/deepseek/deepseek-chat-v3-0324")

agent = CodeAgent(tools=[], model= LiteLLMModel("vertex_ai/gemini-2.5-flash-preview-05-20",
))


answer = agent.run("What is the cube of 2?")
print(answer)
