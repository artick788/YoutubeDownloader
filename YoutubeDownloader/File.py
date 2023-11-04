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

    def _get_value(self, field: str, f) -> str:
        if field in f.tags:
            l = f.tags[field]
            if len(l) > 0:
                return str(l[0])

        return ""

    def read_tags(self, file_path: str):
        f = taglib.File(file_path)
        self.artist = self._get_value("ARTIST", f)
        self.songname = self._get_value("TITLE", f)
        self.album = self._get_value("ALBUM", f)
        self.genre = self._get_value("GENRE", f)
        self.bpm = self._get_value("BPM", f)
        self.key = self._get_value("TKEY", f)

    def save_tags(self, file_path: str):
        f = taglib.File(file_path)
        f.tags["ARTIST"] = self.artist
        f.tags["TITLE"] = self.songname
        f.tags["ALBUM"] = self.album
        f.tags["GENRE"] = self.genre
        f.tags["BPM"] = self.bpm
        f.tags["TKEY"] = self.key

        f.save()
