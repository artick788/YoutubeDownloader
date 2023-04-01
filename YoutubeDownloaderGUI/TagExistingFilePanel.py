import imgui
from YoutubeDownloader import MusicFactory as mf
from .GuiState import GuiState
import tkinter as tk
from tkinter import filedialog

tkInit: bool = False


class TagExistingFilePanel:
    def __init__(self, factory: mf.MusicFactory):
        global tkInit
        self.factory = factory
        self.file = ""

        if not tkInit:
            root = tk.Tk()
            root.withdraw()
            tkInit = True

    def draw(self):
        return_state = GuiState.TAG_EXISTING
        imgui.begin("Download", False, imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_TITLE_BAR)
        if self.file == "":
            if imgui.button("Select file", 210, 20):
                self.file = filedialog.askopenfilename()
        else:
            pass
        imgui.new_line()
        if imgui.button("Back to menu", 210, 20):
            return_state = GuiState.MENU
        if imgui.button("Exit", 210, 20):
            return_state = GuiState.EXIT
        imgui.end()
        return return_state