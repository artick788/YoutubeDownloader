import uuid

import yt_dlp
from .File import *


def mp3_adjust_volume(file_path: str):
    # set volume to lowest possible value
    subprocess.call(["mp3gain", "-r", "-k", "-s", "i", file_path])


def mp3_download_from_youtube(url: str, file: MusicFile) -> str:
    output_file: str = file.artist + " - " + file.songname + ".mp3"

    rand = str(uuid.uuid4())

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': 'output' + rand + '.%(ext)s',
        'extractaudio': True,
        'prefer-ffmpeg': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    tries: int = 4
    while tries > 0:
        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])
                temp_name: str = 'output' + rand
                stream = ffmpeg.input(temp_name + '.m4a')
                stream = ffmpeg.output(stream, temp_name + ".mp3")

                # rename
                os.rename(temp_name + ".mp3", output_file)

                # tag file
                file.save_tags(output_file)

                # adjust volume
                # mp3_adjust_volume(output_file)

                print("MP3 download successful: " + output_file)
                return output_file
        except Exception as e:
            print("MP3 download failed: " + str(e) + " \nTries: " + str(tries))
            tries -= 1
        except KeyboardInterrupt:
            print("MP3 download interrupted\nTries: " + str(tries))
            tries -= 1
        except:
            print("MP3 download failed: no further details, \nTries: " + str(tries))
            tries -= 1

    return ""


