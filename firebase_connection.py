import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
class Firebase:

    ##Logging into the db with credetials and initializing connection with object db
    def get_connection(path):
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        return db

