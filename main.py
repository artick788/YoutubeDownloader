from YoutubeDownloader import YoutubeDownloader as ydl
import taglib


def main():
    desc = ydl.DownloadDesc()
    desc.file_format = ydl.FileFormat.WAV
    desc.url = "https://youtu.be/DxzdRri8o6o"
    desc.artist = "Zedd"
    desc.songname = "Squid game & Do It To It"

    ydl.download(desc)


if __name__ == '__main__':
    main()
