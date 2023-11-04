from tkinter import filedialog

import imgui
from YoutubeDownloader import MusicFactory as mf
from .GuiState import GuiState


class DownloadPanel:
    def __init__(self, factory: mf.MusicFactory):
        self.factory = factory
        self.url = ""
        self.output_path = ""
        self.song = mf.MusicFile()

        self.reset_artist: bool = True
        self.reset_songname: bool = True
        self.reset_album: bool = True
        self.reset_genre: bool = True
        self.reset_bpm: bool = True
        self.reset_key: bool = True

    def draw(self):
        imgui.begin("Download", False, imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_TITLE_BAR)
        self.url = imgui.input_text("URL", self.url, 256)[1]

        imgui.text("Tags")
        self.song.artist = imgui.input_text("Artist", self.song.artist, 256)[1]
        imgui.same_line()
        self.reset_artist = imgui.checkbox("Reset Artist", self.reset_artist)[1]
        self.song.songname = imgui.input_text("Songname", self.song.songname, 256)[1]
        imgui.same_line()
        self.reset_songname = imgui.checkbox("Reset Songname", self.reset_songname)[1]
        self.song.album = imgui.input_text("Album", self.song.album, 256)[1]
        imgui.same_line()
        self.reset_album = imgui.checkbox("Reset Album", self.reset_album)[1]
        self.song.genre = imgui.input_text("Genre", self.song.genre, 256)[1]
        imgui.same_line()
        self.reset_genre = imgui.checkbox("Reset Genre", self.reset_genre)[1]
        self.song.bpm = imgui.input_text("BPM", self.song.bpm, 256)[1]
        imgui.same_line()
        self.reset_bpm = imgui.checkbox("Reset BPM", self.reset_bpm)[1]
        self.song.key = imgui.input_text("Key", self.song.key, 256)[1]
        imgui.same_line()
        self.reset_key = imgui.checkbox("Reset Key", self.reset_key)[1]

        imgui.new_line()
        if imgui.button("set output path", 210, 20):
            self.output_path = filedialog.askdirectory()
        if self.output_path != "":
            imgui.text("Output path: " + self.output_path)
        imgui.new_line()

        if imgui.button("Download", 100, 20):
            self.factory.download_from_youtube(self.url, self.song, self.output_path)
            self.clear_values()
        imgui.same_line()
        if imgui.button("Clear", 100, 20):
            self.url = ""
            self.clear_values()
        imgui.new_line()
        return_state = GuiState.DOWNLOAD
        if imgui.button("Back to menu", 210, 20):
            return_state = GuiState.MENU
        if imgui.button("Exit", 210, 20):
            return_state = GuiState.EXIT
        imgui.end()
        return return_state

    def clear_values(self):
        self.url = ""
        if self.reset_artist:
            self.song.artist = ""
        if self.reset_songname:
            self.song.songname = ""
        if self.reset_album:
            self.song.album = ""
        if self.reset_genre:
            self.song.genre = ""
        if self.reset_bpm:
            self.song.bpm = ""
        if self.reset_key:
            self.song.key = ""
