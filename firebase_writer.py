import firebase_connection, recipe

class FirebaseWriter: 
    ##writes to firestore db
    def firebase_write(db, recipe_obj):
        doc_ref = db.collection(u'recipes').document() ##test needs to be recipe ID
        doc_ref.set({
            u'url' : recipe_obj.get_url(),
            u'name' : recipe_obj.get_name(),
            u'description' : recipe_obj.get_description(),
            u'author' : recipe_obj.get_author(),
            u'servings' : recipe_obj.get_servings(),
            u'ingredients' : recipe_obj.get_ingredients(),
            u'steps' : recipe_obj.get_steps(),
            })