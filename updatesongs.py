from connect import *
 
def update_songs():
    try:
        # SongID is primary key field
 
        songID = int(input("Enter the SongID to update a record: "))
        dbCursor.execute(f"SELECT * FROM songs WHERE SongID = {songID}")
 
        #The fetchone fecthes a unique(one) record
        row = dbCursor.fetchone()
        #None is a single object to check if a value is present
        if row == None:
            print(f"No record with the SongID {songID} exists")
        else:
            fieldname = input("Enter the field (Artist or Title or Genre) ").title()
            fieldValue =input(f"Enter the value for {fieldname}: ")
            
            dbCursor.execute(f"UPDATE songs SET {fieldname} = {fieldValue} WHERE SongID = {songID}")
            dbCon.commit()
            print(f"{songID} updated")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")
if __name__ == "__main__":       
    update_songs()