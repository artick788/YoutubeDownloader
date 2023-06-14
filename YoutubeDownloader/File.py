import youtube_dl
import ffmpeg
import os
import subprocess
import taglib


class FileFormat:
    WAV = 1
    MP3 = 2


class MusicFile:
    def __init__(self):
        self.artist: str = ""
        self.songname: str = ""
        self.album: str = ""
        self.genre: str = ""
        self.bpm: str = ""
        self.key: str = ""
        self.format: int = FileFormat.MP3

    def save_tags(self, file_path: str):
        f = taglib.File(file_path)
        f.tags["ARTIST"] = self.artist
        f.tags["TITLE"] = self.songname
        f.tags["ALBUM"] = self.album
        f.tags["GENRE"] = self.genre
        f.tags["BPM"] = self.bpm
        f.tags["TKEY"] = self.key

        f.save()
