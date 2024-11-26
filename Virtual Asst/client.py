from openai import OpenAI
# client = OpenAI(api_key ="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"   )
 
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful virtual assistant, answer the questions in short."},
#         {
#             "role": "user",
#             "content": "Write a small poem in enlgish."
#         }
#     ]
# )

# print(completion.choices[0].message)
import openai

# Example using the latest OpenAI library
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! How can you help me?"}
    ]
)

# Extract the assistant's response
print(response['choices'][0]['message']['content'])