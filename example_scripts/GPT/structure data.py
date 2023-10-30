#Parse unstructured data and create tables
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
messages=[{"role":"system", "content": "You will be provided with unstructured data, and your task is to parse it into CSV format."]

def multiline_input():
  input_list=[]
  while True:
    line=input()
    if line:
      input_list.append(line)
    else:
      break
  return '\n'.join(input_list)

def structure_data():
  global messages
  while True:
    user_content=multiline_input()
    messages.append({"role": "user", "content": user_content})
    response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=messages,
  temperature=0,
  max_tokens=512
)
    messages.append({"role": "assistant", "content": response})
    print(f"Assistant: {response}")
    if user_content.lower() in ("quit", "exit"):
      exit(0)

structure_data()