import glfw

from YoutubeDownloader import MusicFactory as mf
from YoutubeDownloader import MusicManagerGui as mmg
from glfw import *
import imgui
from imgui.integrations.glfw import GlfwRenderer
import OpenGL.GL as gl

def fast_download():
    factory = mf.MusicFactory()

    if not glfw.init():
        raise Exception("glfw can not be initialized!")

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    window = glfw.create_window(800, 600, "YoutubeDownloader", None, None)
    glfw.make_context_current(window)

    imgui.create_context()
    imgui.get_io().display_size = 800, 600
    imgui.get_io().fonts.get_tex_data_as_rgba32()
    renderer = GlfwRenderer(window)

    song = mf.MusicFile()
    song.format = mf.FileFormat.WAV
    url: str = ""
    while not glfw.window_should_close(window):
        gl.glClearColor(0.45, 0.55, 0.60, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        glfw.poll_events()
        renderer.process_inputs()
        imgui.new_frame()

        imgui.begin("YoutubeDownloader")
        url = imgui.input_text("URL", url, 256)[1]
        song.artist = imgui.input_text("Artist", song.artist, 256)[1]
        song.songname = imgui.input_text("Songname", song.songname, 256)[1]
        if imgui.button("Download"):
            factory.download_from_youtube(url, song)
            url = ""
            song.artist = ""
            song.songname = ""
        imgui.same_line()
        if imgui.button("Clear"):
            url = ""
            song.artist = ""
            song.songname = ""
        if imgui.button("Exit"):
            glfw.set_window_should_close(window, True)
        imgui.end()

        imgui.end_frame()

        imgui.render()
        renderer.render(imgui.get_draw_data())

        glfw.swap_buffers(window)

    glfw.terminate()


def main():
    fast_download()


if __name__ == '__main__':
    main()
