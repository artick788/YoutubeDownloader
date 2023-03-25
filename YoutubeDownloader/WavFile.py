from .File import *
from .DownloadFromYoutube import download_from_youtube


def wav_download_from_youtube(url: str, file: MusicFile) -> str:
    file_on_disk: str = download_from_youtube(url, file)
    return file_on_disk


