import glfw
import imgui
from imgui.integrations.glfw import GlfwRenderer
import OpenGL.GL as gl
from .MusicFactory import MusicFactory, MusicFile, FileFormat


class MusicManagerGui:
    def __init__(self):
        self.factory = MusicFactory()
        self.song = MusicFile()
        self.song.format = FileFormat.WAV
        self.url: str = ""

        if not glfw.init():
            raise Exception("glfw can not be initialized!")
        else:
            glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
            glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
            self.window = glfw.create_window(800, 600, "YoutubeDownloader", None, None)
            glfw.make_context_current(self.window)

            imgui.create_context()
            imgui.get_io().display_size = 800, 600
            imgui.get_io().fonts.get_tex_data_as_rgba32()
            self.renderer = GlfwRenderer(self.window)

    def run(self):
        while not glfw.window_should_close(self.window):
            gl.glClearColor(0.45, 0.55, 0.60, 1)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

            glfw.poll_events()
            self.renderer.process_inputs()
            imgui.new_frame()

            imgui.begin("YoutubeDownloader")
            self.url = imgui.input_text("URL", self.url, 256)[1]
            self.song.artist = imgui.input_text("Artist", self.song.artist, 256)[1]
            self.song.songname = imgui.input_text("Songname", self.song.songname, 256)[1]
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
            if imgui.button("Exit"):
                glfw.set_window_should_close(self.window, True)
            imgui.end()

            imgui.end_frame()

            imgui.render()
            self.renderer.render(imgui.get_draw_data())


