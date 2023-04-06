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

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message_history
        )

        reply_content = completion.choices[0].message.content
        message_history.append(assistant_content(reply_content))
        
    except openai.error.APIError as e:
        print("Received API error:", str(e))
        reply_content = f"Received API error:{e}"

    except Exception as e:
        print("Received unhandled exception:", str(e))
        reply_content = f"Received unhandled exception:{e}"


    response = reply_content

    return response, message_history