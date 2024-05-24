import firebase_admin
from firebase_admin import credentials
from django.conf import settings
import json
from firebase_admin import credentials, db

firebase_app = None
print(settings.FIREBASE_CREDENTIALS_FILE)
print(settings.FIREBASE_CREDENTIALS_JSON)
print(settings.FIREBASE_STORAGE_BUCKET)

def get_firebase_app():
    global firebase_app
    if firebase_app is None:
        if hasattr(settings, 'FIREBASE_CREDENTIALS_FILE') and settings.FIREBASE_CREDENTIALS_FILE:
            cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_FILE)
        elif hasattr(settings, 'FIREBASE_CREDENTIALS_JSON') and settings.FIREBASE_CREDENTIALS_JSON:
            cred = credentials.Certificate(json.loads(settings.FIREBASE_CREDENTIALS_JSON))
        else:
            raise ValueError("Firebase credentials not found. Set FIREBASE_CREDENTIALS_FILE or FIREBASE_CREDENTIALS_JSON in Django settings.")

        try:
            print('Storage Bucket:', settings.FIREBASE_STORAGE_BUCKET)
            firebase_app = firebase_admin.get_app()
        except ValueError:
            firebase_app = firebase_admin.initialize_app(cred, {
                'storageBucket': 'plantsdemo-6bb9b.appspot.com',
                'databaseURL': 'https://plantsdemo-6bb9b-default-rtdb.asia-southeast1.firebasedatabase.app/',
            })
            # Get a reference to the Realtime Database
        

    return firebase_app

firebase_app = get_firebase_app()
print(firebase_app.services)
