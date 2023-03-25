import uuid
import yt_dlp
from .File import *


def get_extension(format: int) -> str:
    if format == FileFormat.WAV:
        return "wav"
    elif format == FileFormat.MP3:
        return "mp3"
    else:
        return "mp3"


def download_from_youtube(url: str, file: MusicFile) -> str:
    file_format: str = get_extension(file.format)
    output_file: str = file.artist + " - " + file.songname + "." + file_format

    rand = str(uuid.uuid4())

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': 'output' + rand + '.%(ext)s',
        'addmetadata': True,
        'extractaudio': True,
        'prefer-ffmpeg': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': file_format,
            'preferredquality': '320',
        }],
    }
    tries: int = 4
    while tries > 0:
        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])
                temp_name: str = 'output' + rand
                stream = ffmpeg.input(temp_name + '.m4a')
                stream = ffmpeg.output(stream, temp_name + "." + file_format)

                # rename
                os.rename(temp_name + "." + file_format, output_file)

                # tag file
                file.save_tags(output_file)

                print("Download successful: " + output_file)
                return output_file
        except Exception as e:
            print("Download failed: " + str(e) + " \nTries: " + str(tries))
            tries -= 1
        except KeyboardInterrupt:
            print("Download interrupted\nTries: " + str(tries))
            tries -= 1
        except:
            print("Download failed: no further details, \nTries: " + str(tries))
            tries -= 1

    return ""