import openai

openai.api_key = "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"

model_engine = "gpt-3.5-turbo"


def createResponse(user_speech):
    messages = [
        {"role": "system", "content": "You are a scary skeleton AI stuck inside a computer. Act very dark and eerie. To the best of your knowledge, act as scary as possible."},
        {"role": "user", "content": user_speech}
    ]

    completion = openai.ChatCompletion.create(
        model=model_engine,
        messages=messages,
        max_tokens=50,
        temperature=0.7,
    )

    response = completion.choices[0].message['content']
    print(response)
    return response


