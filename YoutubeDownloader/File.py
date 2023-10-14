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

    def read_tags(self, file_path: str):
        f = taglib.File(file_path)
        self.artist = f.tags.get("ARTIST", [""])[0]
        self.songname = f.tags.get("TITLE", [""])[0]
        self.album = f.tags.get("ALBUM", [""])[0]
        self.genre = f.tags.get("GENRE", [""])[0]
        self.bpm = f.tags.get("BPM", [""])[0]
        self.key = f.tags.get("TKEY", [""])[0]

    def save_tags(self, file_path: str):
        f = taglib.File(file_path)
        f.tags["ARTIST"] = self.artist
        f.tags["TITLE"] = self.songname
        f.tags["ALBUM"] = self.album
        f.tags["GENRE"] = self.genre
        f.tags["BPM"] = self.bpm
        f.tags["TKEY"] = self.key

        f.save()
