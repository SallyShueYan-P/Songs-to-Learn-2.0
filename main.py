""""
Name: Sally Pang Shue Yan
Date: 14 Sep 2022
Brief Project Description:
This app is called SongsToLearnApp that stores and display the user's songs along with songs' details and songs' status.
With valid inputs, user is able to add new songs to the current songs file.
Additionally, user may choose to sort the songs by artist, title, year, and song's status.
Furthermore, when the user chooses to quit the application, it will automatically save the latest version of all songs in a csv file.
GitHub URL: https://github.com/JCUS-CP1404/assignment-2---songs-sallyshueyan
"""

from kivy.app import App
from song import Song
from songcollection import SongCollection
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.uix.button import Button

FILENAME = "songs.csv"
SORT_CHOICE = {'Artist': "artist", 'Title': "title", 'Year': "year", 'Learned': "is_learned"}


class SongsToLearnApp(App):
    """SongsToLearnApp is an app to display, add and change songs' status depending on user's choice."""
    current_choice = StringProperty()
    sort_choices = ListProperty()

    def __init__(self, **kwargs):
        """Construct main Kivy app."""
        super().__init__(**kwargs)
        self.song_collection = SongCollection()
        self.song_collection.load_songs(FILENAME)

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Songs To Learn 2.0"
        self.root = Builder.load_file('app.kv')
        self.sort_choices = SORT_CHOICE
        self.current_choice = self.sort_choices[0]  # sort on default: Artist
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from list of Song objects and add them to the GUI."""
        self.root.ids.entries_box.clear_widgets()

        for song in self.song_collection.songs:
            temp_button = Button(text=str(song))
            temp_button.song = song
            self.root.ids.entries_box.add_widget(temp_button)

            if song.is_learned:
                temp_button.background_color = (0.529, 0.808, 1, 2)
            else:
                temp_button.background_color = (1, 0.510, 0.671, 2)

            temp_button.bind(on_release=self.press_entry)

        self.root.ids.songs_status.text = f"To learn: {self.song_collection.count_unlearned_song()}. Learned: {self.song_collection.count_learned_song()}"

    def sort_songs(self, choice):
        """Sort songs based on user's choice."""
        self.song_collection.sort(SORT_CHOICE[choice])
        self.create_widgets()

    def press_entry(self, instance):
        """Handle pressing buttons, changing song's status and updating display."""
        song = instance.song

        if song.is_learned:
            song.unlearned_song()
            self.root.ids.output_label.text = f"You need to learn {song.title}"
        else:
            song.learned_song()
            self.root.ids.output_label.text = f"You have learned {song.title}"

        self.root.ids.songs_status.text = f"To learn: {self.song_collection.count_unlearned_song()}. Learned: {self.song_collection.count_learned_song()}"
        self.sort_songs(self.root.ids.sort_by_choice.text)
        instance.text = str(song)

    def add_new_song(self):
        """Add new song based on user's input."""
        new_song_title = str(self.root.ids.new_song_title_input.text).title()
        new_song_artist = str(self.root.ids.new_song_artist_input.text).title()
        new_song_year = self.root.ids.new_song_year_input.text

        if len(new_song_title) == 0 or len(new_song_artist) == 0 or len(new_song_year) == 0:
            self.root.ids.output_label.text = "All fields must be completed"
            return False
        try:
            new_song_year = int(new_song_year)
            if new_song_year < 0:
                self.root.ids.output_label.text = "Year must be >= 0"
                return False
        except ValueError:
            self.root.ids.output_label.text = "Please enter a valid number"
            return False

        new_song = Song(new_song_title, new_song_artist, new_song_year, False)
        self.song_collection.add_song(new_song)
        self.sort_songs(self.root.ids.sort_by_choice.text)
        self.clear_input()

    def clear_input(self):
        """Clear all texts in the title, artist, year and output label."""
        self.root.ids.new_song_title_input.text = " "
        self.root.ids.new_song_artist_input.text = " "
        self.root.ids.new_song_year_input.text = " "
        self.root.ids.output_label.text = ""

    def on_stop(self):
        """Save all modification to csv file after user quits."""
        self.song_collection.save_song(FILENAME)


if __name__ == '__main__':
    SongsToLearnApp().run()
