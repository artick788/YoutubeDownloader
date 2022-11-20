from .File import *


def mp3_download_from_youtube(url: str, file: MusicFile) -> str:
    output_file: str = file.artist + " - " + file.songname + ".mp3"

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': 'output.%(ext)s',
        'extractaudio': True,
        'addmetadata': True,
        'prefer-ffmpeg': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])
        stream = ffmpeg.input('output.m4a')
        stream = ffmpeg.output(stream, "output.mp3")

        # rename
        os.rename("output.mp3", output_file)

        # tag file
        file.save_tags(output_file)

    return output_file


