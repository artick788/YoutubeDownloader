from YoutubeDownloader import MusicFactory as mf


def main():
    song = mf.MusicFile()
    song.artist = "Imanbek"
    song.format = mf.FileFormat.MP3
    song.songname = "Belly Dancer"
    url: str = "https://youtu.be/bEacVcAtiKU"

    factory = mf.MusicFactory()
    factory.download_from_youtube(url, song)


if __name__ == '__main__':
    main()
