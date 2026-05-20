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

# Add the application data
question = input("Ask your questions on python to your study assistant: ")

# Build the prompt
study_prompt = f"""
You are an expert on the python language.
Whenever certain questions are asked, you need to provide response in below format:
- Concept
- Example code showing the concept implementation
- Explanation of the example code and how the concept is done for the user to understand better

Provide answer for the question: {question}
"""
messages = [{"role": "user", "content": study_prompt}]

# Define the application function for completion
def get_completion(messages):
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0,
        max_tokens=1024
    )
    return response.choices[0].message.content

# Print response
print(get_completion(messages))