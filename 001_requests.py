# Install deps
# %pip install anthropic python-dotenv

# Load env variables
from email.mime import message

from dotenv import load_dotenv
load_dotenv()

# create an api client
from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-5"

def add_user_message(messages, text):
    messages.append({
        "role": "user",
        "content": text
    })
    return messages

def add_assistant_message(messages, text):
    messages.append({
        "role": "assistant",
        "content": text
    })
    return messages

def chat(messages, system_prompt=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system_prompt:
        params["system"] = system_prompt

    message = client.messages.create(**params)
    return message.content[message.content.__len__() - 1].text

# make request
system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

messages = []
index = 0

while True:
    user_input = input("> ")

    add_user_message(messages, user_input)
    answer = chat(messages, system_prompt) 
    print(answer)

    add_assistant_message(messages, answer)