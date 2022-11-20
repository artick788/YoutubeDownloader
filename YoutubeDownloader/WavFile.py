from .File import *


def wav_download_from_youtube(url: str, file: MusicFile) -> str:
    output_file: str = file.artist + " - " + file.songname + ".wav"

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': 'output.%(ext)s',
        'extractaudio': True,
        'addmetadata': True,
        'prefer-ffmpeg': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav'
        }],
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])
        stream = ffmpeg.input('output.m4a')
        stream = ffmpeg.output(stream, 'output.wav')

        # rename
        os.rename('output.wav', output_file)
        # tag file
        file.save_tags(output_file)

    return output_file


