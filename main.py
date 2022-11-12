from YoutubeDownloader import YoutubeDownloader as ydl
import music_tag


def main():
    desc = ydl.DownloadDesc()
    desc.file_format = ydl.FileFormat.WAV
    desc.url = "https://youtu.be/CDo3CGxfNIw"
    desc.artist = "Skrillex"
    desc.songname = "Tears"

    ydl.download(desc)


if __name__ == '__main__':
    file = music_tag.load_file("Skrillex - Tears.wav")
    file['tracktitle'] = "Tears"
    file['artist'] = "Skrillex"

    file.save()
#     main()
