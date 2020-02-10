import websitescraper, recipe, firebase_connection, firebase_writer
from firebase_connection import Firebase
from websitescraper import Webscraper
from firebase_writer import FirebaseWriter


def main():
    url = Webscraper.get_url()
    recipeList = Webscraper.connect_to_webpage(url)
    recipe_obj = Webscraper.create_recipe_object(recipeList, url)
    db = Firebase.get_connection("/home/sierra/senior project/firebase/adminsdk.json")
    FirebaseWriter.firebase_write(db, recipe_obj)
    print('wrote')

main()
