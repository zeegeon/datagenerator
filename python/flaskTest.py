import os
import requests
import openai

response = requests.post(
     "https://api.openai.com/v1/chat/completions",
     headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"},
     json={"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "야!"}]},
)

response.json()
"""{'id': 'chatcmpl-76qTg3W2m8YYuAxAbe1DTEk0vsdJe', 'object': 'chat.completion', 'created': 1681866048, 'model': 'gpt-3.5-turbo-0301', 'usage': {'prompt_tokens': 10, 'completion_tokens': 19, 'total_tokens': 29}, 'choices': [{'message': {'role': 'assistant', 'content': '네? 제가 도움을 드릴 수 있나요?'}, 'finish_reason': 'stop', 'index': 0}]}"""

response.json()["choices"][0]["message"]["content"]
"수신된 메시지만 추출"


openai.api_key = os.getenv("키")
response2 = openai.ChatCompletion.create(
     model="gpt-3.5-turbo", messages=[{"role": "user", "content": "야!"}]
)

response2.json()["choices"][0]["message"]["content"]