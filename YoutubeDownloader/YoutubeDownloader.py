import youtube_dl
import ffmpeg

class FileFormat:
    MP3 = 1
    WAV = 2


class DownloadDesc:
    def __int__(self):
        self.url: str = ""
        self.artist: str = ""
        self.songname: str = ""
        self.file_format = FileFormat.MP3


def format_to_string(form) -> str:
    if form == FileFormat.WAV:
        return "wav"
    elif form == FileFormat.MP3:
        return "mp3"


def download(desc: DownloadDesc):
    output_file: str = desc.artist + " - " + desc.songname + "." + format_to_string(desc.file_format)

    post_processors = []
    if desc.file_format == FileFormat.MP3:
        post_processors = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    elif desc.file_format == FileFormat.WAV:
        post_processors = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav'
        }]

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': 'output.%(ext)s',
        'extractaudio': True,
        'addmetadata': True,
        'prefer-ffmpeg': True,
        'postprocessors':post_processors,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([desc.url])
        stream = ffmpeg.input('output.m4a')
        stream = ffmpeg.output(stream, output_file)


