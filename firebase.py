import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firebase:

    ##Logging into the db with credetials and initializing connection with object db
    cred = credentials.Certificate("/home/sierra/senior project/firebase/adminsdk.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()


    ##writes to firestore db
    quote = "dude, wassaup"
    author = "Thong Lam"
    doc_ref = db.collection(u'sample').document(u'test')
    doc_ref.set({
        u'quote' : quote,
        u'author' : author,
        })
