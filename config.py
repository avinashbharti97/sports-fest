import os
from enum import Enum

DB_PATH = os.path.join(os.path.dirname(__file__), 'sports.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
HOST = '0.0.0.0'
PORT = 8080

PHOTOS_UPLOAD_FOLDER = 'photos'
DOCUMENTS_UPLOAD_FOLDER = 'documents'
ALLOWED_PHOTO_EXTENTIONS = set(['jpg', 'jpeg', 'png'])
ALLOWED_DOCUMENT_EXTENTIONS = set(['pdf'])
class ActivityType(Enum):
    ADDED_EVENT = 1
    ADDED_PHOTO = 2
    ADDED_DOCUMENT = 3
    ADDED_RESULT = 4
    ADDED_FEST = 5
    ADDED_PERSON = 6

sqlite = {
    'CREATE_ENGINE_URL': 'sqlite:///{}'.format(DB_PATH)
}
