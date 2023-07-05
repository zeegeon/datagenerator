import requests
import json

key = open('key.txt', 'r').read() #key

prompt = "한국인 20대 여성에 대한 하루 동안의 소비내역 데이터를 json형식으로 예시를 1개 만들어줘"

print("데이터 만드는 중...")
response = requests.post(
     "https://api.openai.com/v1/chat/completions",          # chatgpt API address
     headers={"Authorization": f"Bearer {key}"},            # 인증키
     json={"model": "gpt-3.5-turbo",                        # 모델
           "messages": [{"role": "user",            # role 속성 : user : user, assistant: gpt, system : situation
                          "content": prompt}        # 대화형으로 작성 가능
                          ]},
)

""" 
출력 파일 전체 형식 예시
{'id': 'chatcmpl-76qTg3W2m8YYuAxAbe1DTEk0vsdJe', 'object': 'chat.completion', 'created': 1681866048, 
'model': 'gpt-3.5-turbo-0301',
'usage': {'prompt_tokens': 10, 'completion_tokens': 19, 'total_tokens': 29}, 
'choices': [{'message': 
            {'role': 'assistant', 'content': '네? 제가 도움을 드릴 수 있나요?'}, 
            'finish_reason': 'stop', 'index': 0}]
}
"""
contents = response.json()["choices"][0]["message"]["content"]
#print(response.json())
print(contents) #메시지만 추출

#contents data
testContents = '''{
  "날짜": "2022-01-01",
  "소비내역": [
    {
      "카테고리": "식비",
      "내용": "점심",
      "금액": 7000
    },
    {
      "카테고리": "쇼핑",
      "내용": "의류",
      "금액": 50000
    },
    {
      "카테고리": "교통",
      "내용": "지하철",
      "금액": 2500
    },
    {
      "카테고리": "문화",
      "내용": "영화",
      "금액": 10000
    },
    {
      "카테고리": "기타",
      "내용": "카페",
      "금액": 4000
    }
  ]
}'''

json_test = json.loads(testContents)
print(json_test['소비내역'][0])
