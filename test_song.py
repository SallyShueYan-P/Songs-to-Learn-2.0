"""
Name: Sally Pang Shue Yan
CP1404 - Assignment 2
Date started: 10 Sep 2022
Create class for song.
GitHub URL: https://github.com/JCUS-CP1404/assignment-2---songs-sallyshueyan
"""

from song import Song


def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert not default_song.is_learned

    # Test initial-value song
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print(initial_song)

    # Test new-value song
    new_song = Song("Afterglow", "Taylor Swift", 2019, False)
    print(new_song)

    # Test marking song from learned status to unlearned status.
    initial_song.unlearned_song()
    print(initial_song)

    # Test marking song from unlearned status to learned status.
    new_song.learned_song()
    print(new_song)


run_tests()
