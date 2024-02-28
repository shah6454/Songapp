from connect import *
 
def all_songs():
    try:
        # try to execute the sql statement below
        dbCursor.execute("SELECT * FROM songs")
 
        # fetch all selected data(rows)
        allsongs = dbCursor.fetchall() # Fetchall fetches all the rows from the table
 
        if allsongs:
            # format output
            print("SongID | Title | Artist | Genre")
            print("-" * 50)
 
            for aSong in allsongs:
                print(f"{aSong[0]:<7} | {aSong[1]:<10} | {aSong[2]:<7} | {aSong[3]:<5}")
        else:
            print("No songs found in the songs table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")
if __name__ == "__main__":
    all_songs()
 