from openai import OpenAI

client = OpenAI(api_key='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')

def gpt(text):
    print('Подождите немного, Ваш запрос обробатывается...')
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                "role": "user",
                "content": text,
            },
        ],
    )
    return completion.choices[0].message.content

while True:
    text = input('Напиши что нибудь: ')
    print(gpt(text))