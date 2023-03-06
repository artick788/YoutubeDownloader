import uuid
from .File import *
from yt_dlp import YoutubeDL


def wav_download_from_youtube(url: str, file: MusicFile) -> str:
    output_file: str = file.artist + " - " + file.songname + ".wav"

    rand = str(uuid.uuid4())

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': 'output' + rand + '.%(ext)s',
        'extractaudio': True,
        'addmetadata': True,
        'prefer-ffmpeg': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav'
        }],
    }

    success: bool = False
    while not success:
        try:
            with ydl.YoutubeDL(options) as ydl:
                ydl.download([url])
                temp_name: str = 'output' + rand
                stream = ffmpeg.input(temp_name + '.m4a')
                stream = ffmpeg.output(stream, temp_name + ".wav")

                # rename
                os.rename(temp_name + ".wav", output_file)

                # tag file
                file.save_tags(output_file)

                # adjust volume
                # wav(output_file)

                success = True
        except Exception as e:
            print("MP3 download failed: " + str(e) + " \nRetrying...")
        except KeyboardInterrupt:
            print("MP3 download interrupted")
            success = False
        except:
            print("MP3 download failed: no further details, \nRetrying...")

    return output_file


