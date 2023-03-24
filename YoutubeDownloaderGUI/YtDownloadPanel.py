import imgui
from YoutubeDownloader import MusicFactory as mf
from .GuiState import GuiState

class DownloadPanel:
    def __init__(self, factory: mf.MusicFactory):
        self.factory = factory
        self.url = ""
        self.song = mf.MusicFile()

        self.reset_url: bool = True
        self.reset_artist: bool = True
        self.reset_songname: bool = True
        self.reset_album: bool = True

    def draw(self):
        imgui.begin("Download", False, imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_TITLE_BAR)
        self.url = imgui.input_text("URL", self.url, 256)[1]
        imgui.same_line()
        self.reset_url = imgui.checkbox("Reset URL", self.reset_url)[1]
        self.song.artist = imgui.input_text("Artist", self.song.artist, 256)[1]
        imgui.same_line()
        self.reset_artist = imgui.checkbox("Reset Artist", self.reset_artist)[1]
        self.song.songname = imgui.input_text("Songname", self.song.songname, 256)[1]
        imgui.same_line()
        self.reset_songname = imgui.checkbox("Reset Songname", self.reset_songname)[1]
        self.song.album = imgui.input_text("Album", self.song.album, 256)[1]
        imgui.same_line()
        self.reset_album = imgui.checkbox("Reset Album", self.reset_album)[1]

        if imgui.button("Download", 100, 20):
            self.factory.download_from_youtube(self.url, self.song)
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
        if self.reset_url:
            self.url = ""
        if self.reset_artist:
            self.song.artist = ""
        if self.reset_songname:
            self.song.songname = ""
        if self.reset_album:
            self.song.album = ""
