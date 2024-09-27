import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("meduck-c6933-firebase-adminsdk-5wa08-73536c990f.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# 다른 파일에서 사용할 수 있도록 db 객체를 내보냅니다
