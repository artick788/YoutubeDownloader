from YoutubeDownloader import MusicFactory as mf


def main():
    song = mf.MusicFile()
    song.format = mf.FileFormat.WAV
    song.artist = "The Opposites"
    song.songname = "Thunder"
    url: str = "https://youtu.be/qTkRehr3iGI"

    factory = mf.MusicFactory()
    factory.download_from_youtube(url, song)


if __name__ == '__main__':
    main()
