import os 
from pathlib import Path 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Api key missing")
client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"
def llm_answer(prompt):
    messages = {
        "role":"user",
        "content":prompt
    }
    messages = [messages]
    response = client.chat.completions.create(model=model,messages=messages)
    ans = response.choices[0].message.content
    return ans

bad_prompt = """
iphone refund

#Role 
You are a support assitant at a mobile/laptop company
#task
you have to classify the issue in one category 
#constraint 
you have to classify the issue in one category from the following categories
1 billing 
2 technical
3 return
#output FORMAT
your answer should be in one word only . the one word should be and of the categories given in constraint .
#example 
for instance if a user complain says he wants a refund for his laptop then the answer should be return
#fallback 
if the issue is unrelated to any category then the answer should be OTHER



"""

print(llm_answer(bad_prompt))