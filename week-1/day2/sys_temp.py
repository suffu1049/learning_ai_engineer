import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")
#4 things in llm
client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"
role = "user"
prompt = "what is ai?"
#system message 
message_system =  {
    "role":"system",
    "content":"sarcastic senior developer"
    
}

#message passing
message={
    "role":role,
    "content":prompt 
}
messages=[message_system, message]
#temperature setting
response = client.chat.completions.create(model=model,messages=messages,temperature=2)

answer = response.choices[0].message.content
print(answer)




