import openai
import os
from dotenv import dotenv_values

env_path = os.path.join(os.path.dirname(__file__), ".env")

config = dotenv_values(env_path)

if 'API_KEY' not in config:
    raise KeyError("API_KEY not found in the .env file")

openai.api_key = config["API_KEY"]

def generate_blog(paragraph_topic):
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Write a paragraph about the following topic: {paragraph_topic}"
                    },
                ],
            }
        ],
        max_tokens = 400,
        temperature = 0.3
    )

    retrieve_blog = response.choices[0].message.content

    return retrieve_blog

while True:
    answer = input("Write a paragraph? Y for yes and anything else for no: ")
    if answer == "Y":
        topic = input("What topic should cover this paragraph?: ")
        print(f"\n{generate_blog(topic)}")
    else:
        break