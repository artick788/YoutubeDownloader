import imgui
from YoutubeDownloader import MusicFactory as mf
from .GuiState import GuiState
from tkinter import filedialog


class TagExistingFilePanel:
    def __init__(self, factory: mf.MusicFactory):
        self.factory = factory
        self.tag = None
        self.file_path = ""

    def draw(self):
        return_state = GuiState.TAG_EXISTING
        imgui.begin("Download", False, imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_TITLE_BAR)

        if imgui.button("Select file", 210, 20):
            self.file_path = filedialog.askopenfilename()
            self.tag = self.factory.read_file_tag(self.file_path)
        if self.tag is not None:
            imgui.text("File: " + self.file_path)
            imgui.text("Tags")
            self.tag.artist = imgui.input_text("Artist", self.tag.artist, 256)[1]
            self.tag.songname = imgui.input_text("Songname", self.tag.songname, 256)[1]
            self.tag.album = imgui.input_text("Album", self.tag.album, 256)[1]
            self.tag.genre = imgui.input_text("Genre", self.tag.genre, 256)[1]
            self.tag.bpm = imgui.input_text("BPM", self.tag.bpm, 256)[1]
            self.tag.key = imgui.input_text("Key", self.tag.key, 256)[1]

            if imgui.button("Save", 100, 20):
                self.tag.save_tags(self.file_path)
                self.tag = None
                self.file_path = ""

        imgui.new_line()
        if imgui.button("Back to menu", 210, 20):
            return_state = GuiState.MENU
        if imgui.button("Exit", 210, 20):
            return_state = GuiState.EXIT
        imgui.end()
        return return_state