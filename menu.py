import readsongs, addsongs, updatesongs, deletesong, search

def read_file(file_path):
    try:
        with open(file_path) as readfile:
            rf= readfile.read()
        return rf
    
    except FileNotFoundError as nf:
        print(f"file not found: {nf}")
# Testing file path    
# print(read_file("Pt9_10Db/menuOptions.txt"))

def songs_menu():
    option = 0
    optionslist = ["1","2","3","4","5","6"]
    
    menu_choices = read_file("Pt9_10Db/menuOptions.txt")
    
    # repeat the menu options until user select the to quit
    while option not in optionslist:
        print(menu_choices)
        # re-assign the option variable a string value 
        option = input("Enter an option from the menu choice above")
        # check if the input provided in options variable is not outside of 1,2,3,4,5,6
        if option not in optionslist:
            print(f"{option} is not a valid choice! ")
    return option

#testing
# print(songs_menu())
# create and use a bollean flag variable
mainprogram = True # toggle to flase to exit out of the while loop

while mainprogram: # while True
    # call the songs_menu function and assign to a variable(main_menu)
    main_menu = songs_menu()
    
    # use match case # same as swith in javascript
    match main_menu:
        case "1": # call the readsongs file and the function display all songs
            readsongs.all_songs()
        case "2":
            addsongs.insert_songs()
        case "3":
            updatesongs.update_songs()
        case "4":
            deletesong.delete_asong()
        case "5":
            search.search_song()
        case _:
            mainProgram = False # set mainProgram = False to exit the menu
input("Press enter to exit......")
       
    