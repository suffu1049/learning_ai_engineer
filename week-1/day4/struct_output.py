import os
from pathlib import Path 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Api key missing")
client = Groq(api_key = my_api_key)
model = "llama-3.3-70b-versatile"
role = "user"

##structure krte h ab

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str
    phone_number:int
    
schema = Ticket.model_json_schema()
response_format = {
    "type": "json_object"
    
}
system_prompt = f"""
Extract the personal information from the ticket strictly based on the schema and give a json output
{schema}"""

message_system ={
    "role":"system",
    "content":system_prompt
    
}
text = "hey iam sufiyan i live in vapi my email id is abc@gmail,com and i have issue with my apple watch my gf is beautiful and i love her she cheats on me my phone number is 9737 "

prompt =f"""
This is a customer ticket please extract the perosnal information from this {text}"""
##message me role and content

message = {
    "role":role,
    "content":prompt
}

messages = [message_system,message]
response = client.chat.completions.create(model=model,messages=messages,response_format = response_format)



answer = response.choices[0].message.content
print(answer)
##isko padhte kaise h
import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

##inko pass kr skte h aage !

print(ticket.name)
print(ticket.email)
print(ticket.issue)
print(ticket.phone_number)
