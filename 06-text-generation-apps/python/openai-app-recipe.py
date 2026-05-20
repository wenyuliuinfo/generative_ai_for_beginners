# Import Libraries
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# Configure DeepSeek as used LLM
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)
deployment="deepseek-v4-flash"

# Define the application data
no_recipes = input("Number of recipes (for example, 5): ")
ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")
filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

# Interpolate the number of recipes into the prompt an ingredients
recipes_prompt = f"""
Show me {no_recipes} recipes for a dish with \
the following ingredients: {ingredients}. \
Per recipe, list all the ingredients used, no {filter}: \
"""
messages = [{"role": "user", "content": recipes_prompt}]

# Define the application function for completion
def get_completion(messages):
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0,
        max_tokens=1024
    )
    return response.choices[0].message.content

# Print recipe response
print("\nRecipes: ")
print(get_completion(messages))

old_response = get_completion(recipes_prompt)

shopping = "Produce a shopping list, and please don't include the ingredients that I already have at home: "
shopping_prompt = f"""
Given ingredients at home {ingredients} and these generated recipes: {old_response}, {shopping}
"""
messages = [{"role": "user", "content": shopping_prompt}]

# Print shopping list
print("\nShopping List: \n")
print(get_completion(messages))


