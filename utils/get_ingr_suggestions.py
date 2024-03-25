# get_suggestions.py

from openai import OpenAI

def get_suggestions(messages):
    client = OpenAI()

    ingredients = input("What ingredients do you have? Please list them separated by commas:\n").split(",")
    ingredients = [ingredient.strip() for ingredient in ingredients]
    messages.append(
        {
            "role": "user",
            "content": f"Can you suggest a dish I can make with {', '.join(ingredients)}?"
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
