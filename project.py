import os
from pprint import pprint
import pylast

API_KEY = os.environ['API_KEY']
API_SECRET=os.environ['API_SECRET']

username=""
password_hash = pylast.md5("")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=username, password_hash=password_hash)

user_artist = input("Which artist do you want to know about? ")

artist = network.get_artist(user_artist)

query= input(" Type 'i' for the artist's information.\n Type 't' for the artist$

if query == 'i':
        print ("FOR FULL INFORMATION ON ARTIST")
        pprint (artist.get_bio_content(language="en"))
elif query == 's':
        print ("FOR THE ARTIST'S SUMMARY")
        pprint (artist.get_bio_summary(language="en"))
elif query == 't':
        print ("FOR THE TOP TWO TRACKS")
        pprint (artist.get_top_tracks(limit=2))
elif query == 'a':
        print ("FOR THE TOP TWO ALBUMS")
        pprint (artist.get_top_albums(limit=2))
else:
        print ("Invalid input!")

