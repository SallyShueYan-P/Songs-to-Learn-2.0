"""
Name: Sally Pang Shue Yan
CP1404 - Assignment 2
Date started: 12 Sep 2022
Create class for SongCollection.
GitHub URL: https://github.com/JCUS-CP1404/assignment-2---songs-sallyshueyan
"""

from song import Song
from songcollection import SongCollection


def run_tests():
    """Test SongCollection class."""

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    assert not song_collection.songs  # an empty list is considered False

    # Test loading songs
    print("Test loading songs:")
    song_collection.load_songs('songs.csv')
    print(song_collection)
    assert song_collection.songs  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Song with values
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)

    # Test sorting songs by year
    print("Test sorting - year:")
    song_collection.sort("year")
    print(song_collection)

    # Test sorting songs by artist
    print("Test sorting - artist:")
    song_collection.sort("artist")
    print(song_collection)

    # Test sorting songs by title
    print("Test sorting - title:")
    song_collection.sort("title")
    print(song_collection)

    # Test saving songs
    song_collection.save_song("songs.csv")

    # Test counting songs' status
    learned_songs = song_collection.count_learned_song()
    unlearned_songs = song_collection.count_unlearned_song()
    print(f"To learn: {unlearned_songs}. Learned: {learned_songs}")


run_tests()
