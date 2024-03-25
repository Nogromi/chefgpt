from openai import OpenAI
from utils.get_recipe import get_recipe
from utils.get_ingr_suggestions import get_suggestions
from utils.criticize_recipe import criticize_recipe

client = OpenAI()
messages=[]
def chatbot(personality):
    messages.append(personality)
    messages.append(
        {
            "role": "system",
            "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
        }
    )
    messages.append(
                {
                    "role": "user",
                    "content": "introduce yourself in 5 words"
                }
            )
    while True:
        print("Choose an option:")
        print("1. Get a recipe")
        print("2. Get suggestions based on ingredients")
        print("3. Criticize a recipe")
        
        user_choice = input("Enter the number of your choice (1/2/3): ").strip()
        
        if user_choice == "1":
            get_recipe(messages)
        elif user_choice == "2":
            get_suggestions(messages)
        elif user_choice == "3":
            criticize_recipe(messages)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
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
