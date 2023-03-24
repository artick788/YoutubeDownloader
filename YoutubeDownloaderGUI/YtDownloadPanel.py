import imgui
from YoutubeDownloader import MusicFactory as mf
from .GuiState import GuiState

class DownloadPanel:
    def __init__(self, factory: mf.MusicFactory):
        self.factory = factory
        self.url = ""
        self.song = mf.MusicFile()

    def draw(self):
        imgui.begin("Download", False, imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_TITLE_BAR)
        self.url = imgui.input_text("URL", self.url, 256)[1]
        self.song.artist = imgui.input_text("Artist", self.song.artist, 256)[1]
        self.song.songname = imgui.input_text("Songname", self.song.songname, 256)[1]
        self.song.album = imgui.input_text("Album", self.song.album, 256)[1]

        if imgui.button("Download"):
            self.factory.download_from_youtube(self.url, self.song)
            self.url = ""
            self.song.artist = ""
            self.song.songname = ""
        imgui.same_line()
        if imgui.button("Clear"):
            self.url = ""
            self.song.artist = ""
            self.song.songname = ""
        if imgui.button("Back to menu"):
            return GuiState.MENU
        if imgui.button("Exit"):
            return GuiState.EXIT
        imgui.end()

