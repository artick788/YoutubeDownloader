import glfw
from YoutubeDownloader import MusicFactory as mf
import imgui
from imgui.integrations.glfw import GlfwRenderer
import OpenGL.GL as gl
from .YtDownloadPanel import DownloadPanel
from .TagExistingFilePanel import TagExistingFilePanel
from .GuiState import GuiState

import tkinter as tk


class GUI:
    def __init__(self, window_width: int = 800, window_height: int = 600):
        self.window_width: int = window_width
        self.window_height: int = window_height
        self.window_title: str = "YoutubeDownloader"
        self.window = None
        self.renderer = None
        self.factory = mf.MusicFactory()

        self.state = GuiState.MENU

        # only use tkinter for file dialogs
        root = tk.Tk()
        root.withdraw()

        if not glfw.init():
            raise Exception("glfw can not be initialized!")

        self.download_panel = DownloadPanel(self.factory)
        self.tag_existing_panel = TagExistingFilePanel(self.factory)

    def run(self):
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        self.window = glfw.create_window(self.window_width, self.window_height, self.window_title, None, None)
        glfw.set_framebuffer_size_callback(self.window, self.resize_callback)
        glfw.make_context_current(self.window)
        gl.glViewport(0, 0, self.window_width, self.window_height)
        gl.glClearColor(0.45, 0.55, 0.60, 1)

        imgui.create_context()
        imgui.get_io().display_size = self.window_width, self.window_height
        imgui.get_io().fonts.get_tex_data_as_rgba32()
        renderer = GlfwRenderer(self.window)

        while not glfw.window_should_close(self.window):
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

            glfw.poll_events()
            renderer.process_inputs()
            imgui.new_frame()

            imgui.set_next_window_size(self.window_width, self.window_height)
            imgui.set_next_window_position(0, 0)

            if self.state == GuiState.MENU:
                self.menu()
            elif self.state == GuiState.DOWNLOAD:
                self.state = self.download_panel.draw()
            elif self.state == GuiState.TAG_EXISTING:
                self.state = self.tag_existing_panel.draw()
            elif self.state == GuiState.EXIT:
                glfw.set_window_should_close(self.window, True)

            imgui.end_frame()

            imgui.render()
            renderer.render(imgui.get_draw_data())

            glfw.swap_buffers(self.window)

        glfw.terminate()

    def menu(self):
        imgui.begin("YoutubeDownloader", False, imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_TITLE_BAR)
        button_width, button_height = self.window_width / 2, 30
        button_x = (self.window_width - button_width) / 2.0
        button_y = (self.window_height - button_height) / 3.0
        imgui.set_cursor_pos_x(button_x)
        imgui.set_cursor_pos_y(button_y)
        if imgui.button("Download From Youtube", button_width, button_height):
            self.state = GuiState.DOWNLOAD

        button_y += button_height + 10
        imgui.set_cursor_pos_x(button_x)
        imgui.set_cursor_pos_y(button_y)
        if imgui.button("Tag existing file", button_width, button_height):
            self.state = GuiState.TAG_EXISTING

        button_y += button_height + 30
        imgui.set_cursor_pos_x(button_x)
        imgui.set_cursor_pos_y(button_y)
        if imgui.button("Exit", button_width, button_height):
            glfw.set_window_should_close(self.window, True)
        imgui.end()

    def resize_callback(self, window, width, height):
        self.window_width = width
        self.window_height = height
        imgui.get_io().display_size = width, height
        gl.glViewport(0, 0, width, height)
