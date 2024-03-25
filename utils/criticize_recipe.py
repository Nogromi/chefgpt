# criticize_recipe.py

from openai import OpenAI

def criticize_recipe(messages):
    client = OpenAI()

    recipe = input("Please provide the recipe you want to criticize:\n")
    messages.append(
        {
            "role": "user",
            "content": f"I'd like your opinion on the recipe: {recipe}"
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
