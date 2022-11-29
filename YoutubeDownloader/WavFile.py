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

    success: bool = False
    while not success:
        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([url])
                stream = ffmpeg.input('output.m4a')
                stream = ffmpeg.output(stream, "output.wav")

                # rename
                os.rename("output.wav", output_file)

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


