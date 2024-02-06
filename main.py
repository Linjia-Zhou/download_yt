if __name__ == '__main__':
    from pytube import YouTube

    # insert youtube link
    # try both youtube and youtu.be links if one of them doesn't work
    link = ''

    video = YouTube(link)

    video = video.streams.get_highest_resolution()

    video.download()

