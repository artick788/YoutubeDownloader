from .File import *
from .DownloadFromYoutube import download_from_youtube


def mp3_adjust_volume(file_path: str):
    # set volume to lowest possible value
    subprocess.call(["mp3gain", "-r", "-k", "-s", "i", file_path])


def mp3_download_from_youtube(url: str, file: MusicFile) -> str:
    file_on_disk: str = download_from_youtube(url, file)
    # if file_on_disk != "":
    #     mp3_adjust_volume(file_on_disk)
    return file_on_disk


