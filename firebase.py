import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firebase:

    ##Logging into the db with credetials and initializing connection with object db

    def __init__(self, db)
        cred = credentials.Certificate("/home/sierra/senior project/firebase/adminsdk.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def get_connection(self, db)
        return self.db


    ##writes to firestore db
    def firebase_write(recipe)
        doc_ref = db.collection(u'recipes').document() ##test needs to be recipe ID
        doc_ref.set({
            u'url' : recipe.get_url(),
            u'name' : recipe.get_name(),
            u'description' : recipe.get_description(),
            u'author' : recipe.get_author(),
            u'servings' : recipe.get_servings(),
            u'ingredients' : recipe.get_ingredients(),
            u'steps' : recipe.get_steps(),
            })
