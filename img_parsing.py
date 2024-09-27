import requests
import uuid
import time
import json
from get_sunday import get_sunday_maple_image_url
from firebase_init import db
from firebase_admin import firestore

secret_key = 'd0p3QnZuRWtlSEJObUhUV1lSSE5qS2JucmlOcFRUVEY='
invoke_url = 'https://0vktw8zczn.apigw.ntruss.com/custom/v1/24892/3a493db72c32963a5a07513e34d3f45270b1580ff8ae3d7f4521547016700005/general'

image_url = get_sunday_maple_image_url()

if len(image_url) != 1:
    raise ValueError("이미지 URL이 하나가 아닙니다.")

headers = {'Content-type': 'application/json', 'X-OCR-SECRET': secret_key}
data = {
    'version': 'v2',
    'requestId': str(uuid.uuid4()),
    'timestamp': int(round(time.time() * 1000)),
    'images': [
        {
            'format': 'jpg',
            'name': 'sunday_maple',
            'url': image_url[0]
        }
    ]
}

response = requests.post(invoke_url, headers=headers, data=json.dumps(data))

data = response.json()

# Firestore에 데이터 저장
doc_ref = db.collection('images').document()  # 새 문서 ID 자동 생성
doc_ref.set({
    'data': data,
    'image_url': image_url,
    'timestamp': firestore.SERVER_TIMESTAMP
})

print(f"데이터가 성공적으로 저장되었습니다. 문서 ID: {doc_ref.id}")
