import youtube_dl
import ffmpeg
import os
import taglib


class FileFormat:
    WAV = 1
    MP3 = 2


class MusicFile:
    def __init__(self):
        self.artist: str = ""
        self.songname: str = ""
        self.album: str = ""
        self.format: int = FileFormat.WAV

    def save_tags(self, file_path: str):
        f = taglib.File(file_path)
        f.tags["ARTIST"] = self.artist
        f.tags["TITLE"] = self.songname
        f.save()