# COMP 1516 - Lab 7
# Vilmor Somera
# 11/11/2022

sports_league = {
    "NFL" : "National Football League (American football",
    "MLB" : "Major League Baseball (Baseball)",
    "NBA" : "National Basketball Association (Basketball)",
    "EPL" : "Premier League (Association football)",
    "NHL" : "National Hockey League (Ice hockey)",
    "MLS" : "Major League Soccer (Association football)",
    "IPL" : "Indian Premier League (Twenty20 cricket)",
    "AFL" : "Australian Football League (Australian rules football)",
    "NRL" : "National Rugby League (Rugby league football)",
    "CFL" : "Canadian Football League (Canadian football)",
}

def delete_league():
    """
    Function prompts user to enter the key name of a league to be deleted.
    """
    key = str(input("Enter Key of League: "))
    key = key.upper()

    if key in sports_league:
        print(f"The {sports_league[key]} has been removed")
        sports_league.pop(key)
    else:
        print(f"There is no league named {key}")
    
def add_league():
    """
    Function prompts user for a key and the val and adds it to the sports_league dictionary
    """
    key = str(input("Enter Key of League: "))
    val = str(input("Enter Description of the New League: "))
    key = key.upper()

    if key in sports_league:
        print(f"{key} is already listed as the {sports_league[key]}")
    else:
        sports_league[key] = val
        print("Your league has been added.")

def get_abbreviations():
    """
    Function creates and returns a list of all sports_leagues keys
    """
    key_list = []
    for key in sports_league:
        key_list.append(key)
    return key_list

def get_league_descriptions_tuple():
    """
    Function creates and returns a tuple of all sports leagues values
    """
    val_list = []
    for key in sports_league:
        val_list.append(sports_league[key])
    return tuple(i for i in val_list)

def get_league_description_set():
    """
    Function returns a set of all sport _leagues keys and values
    """
    league_list = []
    for key in sports_league:
        val = sports_league[key]
        league_list.append(f"{key}:{val}")
    league_sets = set(league_list)
    print(league_sets)




def main():
    # delete_league()
    # add_league()
    get_abbreviations()
    get_league_descriptions_tuple()
    get_league_description_set()

if __name__ == "__main__":
    main()