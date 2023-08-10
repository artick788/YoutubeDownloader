import copy

from .Mp3File import mp3_download_from_youtube, mp3_adjust_volume
from .WavFile import wav_download_from_youtube
from .File import MusicFile, FileFormat
import os, glob, shutil
from concurrent.futures import ThreadPoolExecutor


class MusicFactory:
    BIN_DIR: str = "./bin"
    BINARIES: dict = {
        "FFMPEG": "ffmpeg.exe",
        "FFPLAY": "ffplay.exe",
        "FFPROBE": "ffprobe.exe",
        "MP3GAIN": "mp3gain.exe",
        "WAVGAIN": "wavgain.exe",
        "VORBISGAIN": "vorbisgain.exe",
    }

    def __init__(self):
        self.is_setup: bool = False
        self.check_binaries()
        self.thread_pool = ThreadPoolExecutor(max_workers=5, thread_name_prefix="MusicFactory")

    def __del__(self):
        self.thread_pool.shutdown(wait=True)

    def check_binaries(self):
        # check if binaries are in root
        found: bool = True
        for binary in self.BINARIES.values():
            if not os.path.isfile(binary):
                found = False
                break
        if found:
            self.is_setup = True
            return
        else:
            # check if binaries are in bin folder
            found = True
            for binary in self.BINARIES.values():
                if not os.path.isfile(self.BIN_DIR + "/" + binary):
                    found = False
                    break
                else:
                    shutil.copy(self.BIN_DIR + "/" + binary, binary)
            if found:
                self.is_setup = True
                return
            else:
                raise Exception("Binaries not found")

    def download_from_youtube(self, url: str, music_file: MusicFile):
        if self.is_setup:
            # make sure these are copied and not referenced
            c_url = copy.deepcopy(url)
            c_music_file = copy.deepcopy(music_file)
            if music_file.format == FileFormat.WAV:
                self.thread_pool.submit(wav_download_from_youtube, c_url, c_music_file)
            elif music_file.format == FileFormat.MP3:
                self.thread_pool.submit(mp3_download_from_youtube, c_url, c_music_file)
        else:
            raise Exception("Factory is not setup properly")

    def tag_file(self, file_path, music_file: MusicFile):
        if self.is_setup:
            music_file.save_tags(file_path)
        else:
            raise Exception("Factory is not setup properly")

    def read_file_tag(self, file_path) -> MusicFile:
        if self.is_setup:
            file = MusicFile()
            file.read_tags(file_path)
            return file
        else:
            raise Exception("Factory is not setup properly")

    def adjust_volume(self, file_path, format: FileFormat):
        if self.is_setup:
            if format == FileFormat.WAV:
                pass
            elif format == FileFormat.MP3:
                mp3_adjust_volume(file_path)
        else:
            raise Exception("Factory is not setup properly")



