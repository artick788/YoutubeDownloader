from YoutubeDownloader import YoutubeDownloader as ydl


def main():
    desc = ydl.DownloadDesc()
    desc.file_format = ydl.FileFormat.WAV
    desc.url = "https://youtu.be/CDo3CGxfNIw"
    desc.artist = "Skrillex"
    desc.songname = "Tears"

    ydl.download(desc)


if __name__ == '__main__':
    main()
