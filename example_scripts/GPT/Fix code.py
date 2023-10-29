# Find and fix bugs in source code with the help of GPT4.
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
messages=[{"role":"system", "content": "You will be provided with a piece of Python code, and your task is to find and fix bugs in it."]

def multiline_input():
  input_list=[]
  while True:
    line=input()
    if line:
      input_list.append(line)
    else:
      break
  return '\n'.join(input_list)

def fix_code():
  global messages
  while True:
    user_content=multiline_input()
    messages.append({"role": "user", "content": user_content})
    response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=messages,
  temperature=0,
  max_tokens=1024
)
    messages.append({"role": "assistant", "content": response})
    print(f"Assistant: {response}")
    if user_content.lower() in ("quit", "exit"):
      exit(0)

fix_code()