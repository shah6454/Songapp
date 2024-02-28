from connect import *
def search_song():
        try:
                #ask for the field to search by
            # dbCursor.execute("SELECT * FROM songs")
            dbCursor.execute("SELECT * FROM songs ORDER BY Title DESC")
            dbCursor.execute("SELECT * FROM songs WHERE Genere = 'Pop' OR Genere = 'Classic'''")
            allsongs = dbCursor.fetchall()
            for songs in allsongs:
                   print(songs)
        except sql.OperationalError as e:
                print(f"Errro: {e}")
           
search_song()