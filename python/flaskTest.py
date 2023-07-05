import requests

key = open('key.txt', 'r').read() #key
#print(key)

prompt = "한국인 20대 여성에 대한 하루 동안의 소비내역 데이터를 json형식으로 예시를 1개 만들어줘"

response = requests.post(
     "https://api.openai.com/v1/chat/completions",
     headers={"Authorization": f"Bearer {key}"},
     json={"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}]},
)

#print(response.json())
""" 출력 파일 전체 형식
{'id': 'chatcmpl-76qTg3W2m8YYuAxAbe1DTEk0vsdJe', 'object': 'chat.completion', 'created': 1681866048, 'model': 'gpt-3.5-turbo-0301', 'usage': {'prompt_tokens': 10, 'completion_tokens': 19, 'total_tokens': 29}, 'choices': [{'message': {'role': 'assistant', 'content': '네? 제가 도움을 드릴 수 있나요?'}, 'finish_reason': 'stop', 'index': 0}]}"""

print(response.json()["choices"][0]["message"]["content"])
"""response.json()["choices"][0]["message"]["content"]"""
"수신된 메시지만 추출"