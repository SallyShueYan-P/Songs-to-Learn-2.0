"""
Name: Sally Pang Shue Yan
CP1404 - Assignment 2
Date started: 12 Sep 2022
Create class for SongCollection.
GitHub URL: https://github.com/JCUS-CP1404/assignment-2---songs-sallyshueyan
"""

from song import Song
from operator import attrgetter


class SongCollection:
    """SongCollection class for Song application."""

    def __init__(self):
        """Initialise list of Song objects."""
        self.songs = []  # list of Songs as objects

    def load_songs(self, csv_file):
        """Load records into list of Song objects."""
        with open(csv_file, "r") as in_file:
            for line in in_file.readlines():
                data = line.split(",")
                title = data[0].strip()
                artist = data[1].strip()
                year = int(data[2].strip())
                if data[3].strip() == "u":  # check song's status
                    is_learned = False
                else:
                    is_learned = True
                song = Song(title, artist, year, is_learned)
                self.songs.append(song)
            in_file.close()

    def __str__(self):
        """Return a string representation of Song object."""
        song_str = ""
        if len(self.songs) == 0:
            song_str = "There are no songs in your collection"
        else:
            for i in self.songs:
                song_str = song_str + f"{i}\n"
        return song_str

    def add_song(self, song):
        """Add a Song object to the list of Song objects."""
        new_song = Song(song.title, song.artist, song.year, song.is_learned)
        self.songs.append(new_song)

    def sort(self, key):
        """Sort songs by user's choice and by title."""
        self.songs = sorted(self.songs, key=attrgetter(key, 'title'))

    def save_song(self, csv_file):
        """Save all songs to csv file."""
        with open(csv_file, "w") as out_file:
            for song in self.songs:
                print(f"{song.__repr__()}", file=out_file)
            out_file.close()

    def count_learned_song(self):
        """Count number of songs with song status as learned(l)."""
        songs_learned_count = 0
        for song in self.songs:
            if song.is_learned is True:
                songs_learned_count += 1
        return songs_learned_count

    def count_unlearned_song(self):
        """Count number of songs with song status as unlearned(u)."""
        songs_unlearned_count = 0
        for song in self.songs:
            if song.is_learned is False:
                songs_unlearned_count += 1
        return songs_unlearned_count
