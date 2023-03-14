import openai
import os

from payload_creation import (
        user_content,
    assistant_content,
)

openai.api_key= os.environ.get('CHATTIE_OPEN_AI_KEY')

# -- Openai API
def send_message_to_chattie(input, message_history=[]):
    message_history.append(user_content(input))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )

    reply_content = completion.choices[0].message.content
    message_history.append(assistant_content(reply_content))

    response = reply_content

    return response, message_history