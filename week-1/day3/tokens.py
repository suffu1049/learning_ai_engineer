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
##3three prompts
prompt1 = "what is ai?"
prompt2 = "where is vapi located?"
prompt3 = "What is the hashmap in cpp?"
prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    message={
        "role" : role,
        "content":prompt
    }    
    messages=[message]
    response = client.chat.completions.create(model=model,messages=messages,max_tokens=500)
    # print(response)
    usage = response.usage 
    print(f"prompt:{prompt}->Your tokens:{usage.prompt_tokens} completion_tokens:{usage.completion_tokens} total tokens :{usage.total_tokens} Finish reason:{response.choices[0].finish_reason}")



#system message 
# message_system = {
#     "role":"system",
#     "content":"sarcastic senior developer"
    
# }

#message passing
# message={
#     "role":role,
#     "content":prompt 
# }
# messages=[message]
#temperature setting // tokens settings
# response = client.chat.completions.create(model=model,messages=messages,max_tokens=5000)

# answer = response.choices[0].message.content
# print(answer)




