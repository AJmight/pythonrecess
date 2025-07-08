import requests
import json


response=requests.get("https://api.stackexchange.com/2.3/answers?order=desc&sort=activity&site=stackoverflow")
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit()
for data in response.json()['items']:
    print(f"Answer ID: {data['answer_id']}")
    print(f"Question ID: {data['question_id']}")
    