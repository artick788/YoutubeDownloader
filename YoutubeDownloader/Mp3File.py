from .File import *


def mp3_adjust_volume(file_path: str):
    # set volume to lowest possible value
    subprocess.call(["mp3gain", "-r", "-k", "-s", "i", file_path])


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
    success: bool = False
    while not success:
        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([url])
                stream = ffmpeg.input('output.m4a')
                stream = ffmpeg.output(stream, "output.mp3")

                # rename
                os.rename("output.mp3", output_file)

                # tag file
                file.save_tags(output_file)

                # adjust volume
                # mp3_adjust_volume(output_file)

                success = True
        except Exception as e:
            print("MP3 download failed: " + str(e) + " \nRetrying...")
        except KeyboardInterrupt:
            print("MP3 download interrupted")
            success = False
        except:
            print("MP3 download failed: no further details, \nRetrying...")

    return output_file


