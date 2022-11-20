from .Mp3File import mp3_download_from_youtube, mp3_adjust_volume
from .WavFile import wav_download_from_youtube
from .File import MusicFile, FileFormat
import os, glob, shutil


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
        self.__is_setup: bool = False
        self.__check_binaries()

    def __check_binaries(self):
        # check if binaries are in root
        found: bool = True
        for binary in self.BINARIES.values():
            if not os.path.isfile(binary):
                found = False
                break
        if found:
            self.__is_setup = True
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
                self.__is_setup = True
                return
            else:
                raise Exception("Binaries not found")

    def download_from_youtube(self, url: str, music_file: MusicFile) -> str:
        if self.__is_setup:
            if music_file.format == FileFormat.WAV:
                return wav_download_from_youtube(url, music_file)
            elif music_file.format == FileFormat.MP3:
                return mp3_download_from_youtube(url, music_file)
        else:
            raise Exception("Factory is not setup properly")

    def tag_file(self, file_path, music_file: MusicFile):
        if self.__is_setup:
            music_file.save_tags(file_path)
        else:
            raise Exception("Factory is not setup properly")

    def adjust_volume(self, file_path, format: FileFormat):
        if self.__is_setup:
            if format == FileFormat.WAV:
                pass
            elif format == FileFormat.MP3:
                mp3_adjust_volume(file_path)
        else:
            raise Exception("Factory is not setup properly")



