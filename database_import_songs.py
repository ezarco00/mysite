from flask_app import db
from flask_app import Song
import constants

for song in constants.SONGS:
    db.session.add(
        Song(
            title=song.title,
            artist=song.artist,
            youtube_url=song.youtube_url))

db.session.commit()
