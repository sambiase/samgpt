from decouple import config
import openai

SECRET_KEY = config('SECRET_KEY')
openai.api_key = SECRET_KEY

messages = [
    {"role": "system",
     "content": "You're a recruiter who asks interview questions. You ask one new question after my response"}
]

while True:
    print('*'*23)
    content = input("Please write something: ")
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    messages.append({"role": "assistant", "content": chat_response})
