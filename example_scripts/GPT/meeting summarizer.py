#The following summarizes meeting notes including overall discussion, action items, and future topics.
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
messages=[{"role":"system", "content": "You will be provided with meeting notes, and your task is to summarize the meeting as follows:

-Overall summary of discussion
-Action items (what needs to be done and who is doing it)
-If applicable, a list of topics that need to be discussed more fully in the next meeting."]

def multiline_input():
  input_list=[]
  while True:
    line=input()
    if line:
      input_list.append(line)
    else:
      break
  return '\n'.join(input_list)

def summarize_meeting():
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

summarize_meeting()