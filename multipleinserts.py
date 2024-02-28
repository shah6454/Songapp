from connect import *
from readsongs import *

def multiple_records():
        songs = [
                ('Smooth', 'Oscar Rhythm', 'Blues'),
                ('Peaches', 'Maya Blues', 'Reggae'),
                ('Fancy Like', 'Alice Harmony', 'EDM'),
                ('Don''t You Want Me', 'Finn Melody', 'Folk'),
                ('Don''t You Want Me', 'Jack Beat', 'Classical')
                ]
    
        # write the content found/stored in the sqlInsertScript variable 
        dbCursor.executemany("INSERT INTO songs(Title, Artist, Genre) VALUES(?,?,?)", songs)
        dbCon.commit()
        # now call the all_songs function from the readsongs file to display updated records
        all_songs()
multiple_records()
       