# get_recipe.py

from openai import OpenAI

def get_recipe(messages):
    client = OpenAI()

    dish = input("Type the name of the dish you want a recipe for:\n")
    messages.append(
        {
            "role": "user",
            "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
        }
    )

    model = "gpt-3.5-turbo"

    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )
