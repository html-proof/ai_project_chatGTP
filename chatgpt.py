import openai
import json

def sample_response(input_text):
    user_message =str(input_text).lower()
    openai.api_key = "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"

    while True:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=user_message,
                temperature=0.5,
                max_tokens=1500,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )

            json_object = json.loads(str(response))
            return (json_object['choices'][0]['text'])