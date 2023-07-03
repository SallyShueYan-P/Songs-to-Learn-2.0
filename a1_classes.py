"""
Name: Sally Pang Shue Yan
CP1404 - Assignment 2
Date started: 12 Sep 2022
a1_classes.py has the ability to execute actions such as list songs, add song, complete a song, or quit the program with classes based on user input.
GitHub URL: https://github.com/JCUS-CP1404/assignment-2---songs-sallyshueyan
"""

from song import Song
from songcollection import SongCollection

FILENAME = "songs.csv"
MENU = "Menu:\nL - List songs\nA - Add new song\nC - Complete a song\nQ - Quit"
CHOICE = "L", "A", "C", "Q"


def main():
    """Start of program."""
    songs_collection = SongCollection()
    songs_collection.load_songs(FILENAME)
    print("Songs to Learn 1.0 - by Sally Pang")
    print(f"{len(songs_collection.songs)} songs loaded")
    print(MENU)
    choice = choice_validity(">>> ").upper()

    while choice != "Q":
        verify_choice(choice, songs_collection)
        print(MENU)
        choice = choice_validity(">>> ").upper()

    if choice == "Q":
        songs_collection.save_song(FILENAME)
        print(f"{len(songs_collection.songs)} songs saved to songs.csv\nHave a nice day :)")


def verify_choice(choice, songs_collection):
    """Verify choice to pass in to other functions."""
    if choice == "L":
        display_songs(songs_collection)
    elif choice == "A":
        add_song(songs_collection)
    elif choice == "C":
        complete_song(songs_collection)


def choice_validity(prompt):
    """Check validity of user's input."""
    choice = str(input(prompt)).upper()
    while choice not in CHOICE:
        print("Invalid menu choice")
        choice = str(input(">>> ")).upper()
    return choice


def display_songs(songs_collection):
    """Display all the songs with their details."""
    songs_index = 0
    songs_collection.sort("artist")
    for song in songs_collection.songs:
        if song.is_learned is True:
            print(f"{songs_index:2}.   {song.title:30} - {song.artist:25} ({song.year:4})")
        else:
            print(f"{songs_index:2}. * {song.title:30} - {song.artist:25} ({song.year:4})")
        songs_index += 1
    print(
        f"{songs_collection.count_learned_song()} songs learned, {songs_collection.count_unlearned_song()} songs still to learn")


def add_song(songs_collection):
    """Collect new song's details."""
    song_title = input("Title: ").title()
    while verify_input(song_title) is True:
        song_title = input("Title: ").title()

    artist = input("Artist: ").title()
    while verify_input(artist) is True:
        artist = input("Artist: ").title()

    new_song_validity = False
    while new_song_validity is False:
        try:
            year = int(input("Year: "))
            while year < 0:
                print("Number must be >= 0")
                year = int(input("Year: "))
            new_song_validity = True
        except ValueError:
            print("Invalid input; enter a valid number")
            new_song_validity = False
    print(f"{song_title} by {artist} ({year}) added to song list")
    songs_collection.add_song(Song(song_title, artist, year, False))


def verify_input(new_input):
    """Display message to ensure no blank input."""
    if len(new_input) == 0:
        print("Input can not be blank")
        return True
    else:
        return False


def complete_song(songs_collection):
    """Convert current song to learned (l) status."""
    if songs_collection.count_learned_song() == len(songs_collection.songs):
        print("No more songs to learn!")
    else:
        print("Enter the number of a song to mark as learned")
        choice_validity = False
        while choice_validity is False:
            try:
                choice = int(input(">>> "))
                if choice < 0:
                    print("Number must be >= 0")
                elif choice > len(songs_collection.songs) - 1:  # length function always start at 1
                    print("Invalid song number")
                else:
                    song_index = 0
                    for song in songs_collection.songs:
                        if song_index < choice:
                            song_index += 1
                        elif song_index == choice:
                            if song.is_learned:
                                print(f"You have already learned {song.title}")
                                song_index += 1
                                choice_validity = True
                            elif not song.is_learned:
                                print(f"{song.title} by {song.artist} learned")
                                song_index += 1
                                song.learned_song()
                                choice_validity = True
            except ValueError:
                print("Invalid input; enter a valid number")


main()
