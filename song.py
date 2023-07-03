"""
Name: Sally Pang Shue Yan
CP1404 - Assignment 2
Date started: 10 Sep 2022
Create class for song.
GitHub URL: https://github.com/JCUS-CP1404/assignment-2---songs-sallyshueyan
"""


class Song:
    """Song class for storing details of a song."""

    def __init__(self, title="", artist="", year=0, is_learned=False):
        """Initialise a Song."""
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    def __str__(self):
        """Return a presentable string representation of a Song."""
        if self.is_learned:
            return f'"{self.title}" by {self.artist} ({self.year}) (learned)'
        else:
            return f'"{self.title}" by {self.artist} ({self.year})'

    def __repr__(self):
        """Return a string representation of a Song."""
        if self.is_learned:
            return f'{self.title},{self.artist},{self.year},l'
        else:
            return f'{self.title},{self.artist},{self.year},u'

    def learned_song(self):
        """Mark the song that have learnt."""
        self.is_learned = True

    def unlearned_song(self):
        """Mark the song that have not learnt."""
        self.is_learned = False
