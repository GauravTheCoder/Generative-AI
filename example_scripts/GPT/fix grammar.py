#The following fixes grammar of sentences given.
import os
import openai

messages=[{"role":"system", "content": "You will be provided with statements, and your task is to convert them to standard English."]
openai.api_key = os.getenv("OPENAI_API_KEY")

def multiline_input():
  input_list=[]
  while True:
    line=input()
    if line:
      input_list.append(line)
    else:
      break
  return '\n'.join(input_list)

def fix_grammar():
  global messages
  while True:
    user_content=multiline_input()
    messages.append({"role": "user", "content": user_content})
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0,
    max_tokens=256
)
    messages.append({"role": "assistant", "content": response})
    print(f"Assistant: {response}")
    if user_content.lower() in ("quit", "exit"):
      exit(0)

fix_grammar()
